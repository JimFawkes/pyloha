from base.loader import Loader


class ReqresLoader(Loader):
    def __init__(self, **kwargs):
        self.page = 1
        self.total_pages = 100
        super().__init__(**kwargs)

    def construct_urls(self):
        url = f"{self.base_url}?page={self.page}"

        if hasattr(self, "per_page"):
            url = f"{url}&per_page={self.per_page}"

        return url

    def stop_condition(self):
        return self.page > self.total_pages

    def process_response(self):
        body = self.response.json()
        self.data = body["data"]
        self.page = body["page"] + 1
        self.total_pages = body["total_pages"]
