class BaseManager:
    def __init__(self):
        self._reddit = None

    @property
    def reddit(self):
        return self._reddit

    @reddit.setter
    def reddit(self, value):
        if self._reddit is not None:
            raise RuntimeError("reddit can only be set once and is done automatically")
        self._reddit = value

    def post_refresh_callback(self, authorizer):
        """Called after a refresh token is used.

        :param authorizer: The ``prawcore.Authorizer`` instance used containing
        ``access_token`` and ``refresh_token`` attributes.

        This function will be called after refreshing the access and refresh
        tokens. This callback can be used for saving the updated
        ``refresh_token``.

        """
        raise NotImplementedError("post_refresh_callback must be extended.")

    def pre_refresh_callback(self, authorizer):
        """Called before refreshing PRAW's authorization.

        :param authorizer: The ``prawcore.Authorizer`` instance used containing
        ``access_token`` and ``refresh_token`` attributes.

        This callback can be used to inspect and modify the attributes of the
        ``prawcore.Authorizer`` instance, such as setting the
        ``refresh_token``.

        """
        raise NotImplementedError("pre_refresh_callback must be extended.")


class FileManager(BaseManager):
    def __init__(self, filename):
        """Load and save refresh tokens from a file.

        :param filename: The file the contains the refresh token.

        """
        super().__init__()
        self._filename = filename

    def post_refresh_callback(self, authorizer):
        """Updates the saved copy of the refresh token."""
        with open(self._filename, "w") as fp:
            fp.write(authorizer.refresh_token)

    def pre_refresh_callback(self, authorizer):
        """Loads the refresh token from the file."""
        if authorizer.refresh_token is None:
            with open(self._filename) as fp:
                authorizer.refresh_token = fp.read().strip()
