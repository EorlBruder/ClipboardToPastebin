from smoid.languages import Check, CheckCollection


class HtmlDoctypeCheck (Check):

    def __init__ (self):
        Check.__init__ (self)
        self.name = "Html:Doctype"
        self.example = '<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">'
        self.type = Check.kTYPE_FINAL
        self.add_language("html5")

        self.add_one_time_match("(?:\r|\n|^)<!DOCTYPE (HTML|html) PUBLIC \"", 200)


class HtmlCheckCollection (CheckCollection):
    def __init__ (self):

        self.append(HtmlDoctypeCheck())
