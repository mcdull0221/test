from urllib import request
import re


class Spider:
    url = 'https://www.huya.com/g/lol'
    root_pattern = '<span class="txt">([\s\S]*?</i>)</span>'      # 非贪婪模式
    name_pattern = '<i class="nick" title="([\s\S]*?)">'
    number_pattern = '<i class="js-num">([\s\S]*?)</i>'

    def __fetch_content(self):
        r = request.urlopen(Spider.url)
        htmls = r.read()
        htmls = str(htmls, encoding='utf-8')
        return htmls

    def __analysis(self, htmls):
        # 抓取数据
        root_html = re.findall(Spider.root_pattern, htmls)
        # print(root_html[0])
        anchors = []
        for html in root_html:
            name = re.findall(Spider.name_pattern, html)
            number = re.findall(Spider.number_pattern, html)
            anchor = {'name': name, 'number': number}
            anchors.append(anchor)
        # print(anchors)
        return anchors

    def __refine(self, anchors):
        # 精炼数据
        l = lambda anchor: {
            'name': anchor['name'][0].strip(),
            'number': anchor['number'][0]
        }
        return map(l, anchors)

    def __sort(self, anchors):
        # 排序
        anchors = sorted(anchors, key=self.__sort_seed, reverse=True)
        return anchors

    def __sort_seed(self, anchor):
        # 根据人数排序
        r = re.findall('\d*', anchor['number'])
        number = float(r[0])
        if '万' in anchor['number']:
            number *= 10000
        return number

    def __show(self, anchors):
        for rank in range(0, len(anchors)):
            print('排名 ' + str(rank+1) + ':' + anchors[rank]['name'] + '    ' + anchors[rank]['number'])

    def go(self):
        htmls = self.__fetch_content()
        anchors = self.__analysis(htmls)
        anchors = list(self.__refine(anchors))
        anchors = self.__sort(anchors)
        self.__show(anchors)


if __name__ == '__main__':
    spider = Spider()
    spider.go()
