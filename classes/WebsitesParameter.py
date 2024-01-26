class HtmlTag:
    html_tags = ["class", "id"]

    def __init__(self, tag, name, to_remove=[]):
        if tag not in self.html_tags:
            raise ValueError("tag must be in {}".format(
                self.html_tags), " {tag} passed")
        self.tag = tag
        self.name = name
        self.to_remove = to_remove


class WebsiteParameters:
    def __init__(self, name, title_tag, content_tag):
        self.name = name
        if not isinstance(title_tag, HtmlTag):
            raise ValueError("title_tag must be an instance of HtmlTag")
        self.title_tag = title_tag
        if not isinstance(content_tag, HtmlTag):
            raise ValueError("content_tag must be an instance of HtmlTag")
        self.content_tag = content_tag
