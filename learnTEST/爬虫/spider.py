from urllib import request
import re


class Spider:
    url = 'https://www.huya.com/g/lol'
    root_pattern = '<span class="txt">[\s\S]*?</i></span>'      # 非贪婪模式

    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls

    def __analysis(self, htmls):
        root_html = re.findall(Spider.root_pattern, htmls)
        return root_html

    def go(self):
        htmls = self.__fetch_content()
        self.__analysis(htmls)


if __name__ == '__main__':
    spider = Spider()
    spider.go()
