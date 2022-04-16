from lxml import etree

xmp='''
    <book>
        <id>1</id>
        <name>野花香</name>
        <author>
            <nick id="10086">周大枪</nick>
            <nick id="10010">周结论</nick>
            <prince>
                <nick id="12356">周芷若</nick>
            </prince>
        </author>
    </book>
'''
tree=etree.XML(xmp)
result1=tree.xpath("/book//nick/text()")
print(result1)
