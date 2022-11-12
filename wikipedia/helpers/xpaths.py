class XPATH:
    article_link = '//div[@id="bodyContent"]/descendant::a[re:test(@href, "^/wiki/[^:]*$")]/@href'
    title = '//span[@class="mw-page-title-main"]/text()'
    description = '//div[@class="mw-parser-output"]/p[1]/descendant-or-self::*[self::b or self::p or self::a]/text()'
    image_url = '//div[@class="mw-parser-output"]/table/descendant::img/@src'