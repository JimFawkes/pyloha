import requests


class LoaderError(Exception):
    pass


class Loader:
    def __init__(self, **kwargs):
        self.headers = {"Content-Type": "application/json"}
        self.__dict__.update(**kwargs)

        if not hasattr(self, "base_url"):
            raise LoaderError(f"A base URL is required but not passed")

    def __repr__(self):
        return f"{self.__class__.__name__}(base_url={self.base_url})"

    def __iter__(self):
        return self

    def __next__(self):
        if not self.stop_condition():
            self.url = self.construct_urls()
            self.response = self._make_request()
            self.process_response()
            return self.get_data()
        else:
            raise StopIteration

    def stop_condition(self):
        raise NotImplementedError(
            f"{self.__class__.__name__}.stop_condition(self) is required."
        )

    def construct_urls(self):
        raise NotImplementedError(
            f"{self.__class__.__name__}.construct_urls(self) is required."
        )

    def _make_request(self):
        request = requests.get(self.url, headers=self.headers)
        return request

    def process_response(self):
        raise NotImplementedError(
            f"{self.__class__.__name__}.process_response(self) is required."
        )

    def get_data(self):
        return self.data
