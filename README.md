3.16 embark on a new project
----------------------------------广东省公共资源数据采集--------------------------
1.	主要网站(https://ygp.gdzwfw.gov.cn/#/44/jygg)
全国公共资源交易平台（广东省） 

2.	主要任务
1.	在广东省公共资源平台获取栏目“政府采购”中检索近1个月全部公告，可获取该栏目的各公告标题、公告类型、发布平台以及该月内所有的公告发布时间。  
2.	对网站中该栏目下的所有公告的公告标题、公告类型、发布平台、发布时间、公告内容进行数据爬取。
3.	以上图中“汕头市人民医院2025年08月至2025年09月政府采购意向”为例，所需内容包含：
	公告标题：汕头市人民医院2025年08月至2025年09月政府采购意向
	公告发布时间：2025-08-07 10:47:12
	来源：广东政府采购智慧云平台 政府采购 - 采购意向公开
	公告性质：正常公告
	公告编号：8a7e08649873236301988259f0e7012a
	公告内容：<html> <style> /* 采购意向 宋体，2.5行高，默认16号字 大标题用h2标签，字号为24号加粗 一级标题用h3标签，字号为18号加粗 二级标题用h4标签，字号为16号加粗 三级标题用h5标签，字号为16号加粗，首行缩进28px 段落字号16px，首行缩进28px 普通文字为16号字体 表格标题为加粗，表格字号为16号字体，高度为32px，表格外部上下间距10px，左右居中；单元格内上下间距5px，左右间距8px； 标题加粗，自己改为<strong></strong>或者加样式。 标题段落间距为8px */ .noticeArea{ line-height:2.5; font-size: 16px;text-align: justify;font-family: '宋体';} .noticeArea *{padding:0; margin:0;} .noticeArea h2{font-size: 24px; text-align: center; margin-bottom: 20px;} .noticeArea h3{font-size: 18px;font-weight: normal;line-height:40px;} .noticeArea h4{font-size: 16px;font-weight: normal;line-height:40px;} .noticeArea h5{font-size: 16px;text-indent: 28px;font-weight: .......break-all;\">1</td> <td align=\"left\" style=\"-ms-word-break: break-all;\">物产楼安保管理服务项目</td> <td style=\"-ms-word-break: break-all; text-align: left\"> <div> 标的名称：物产楼安保管理服务项目 </div> <div> 标的数量：1 </div> <div> 主要功能或目标：中标人需按照采购人的安保管理服务需求，为汕头市龙湖区物产楼场地提供安保服务，包括秩序管理服务，车辆管理，人员进驻、管理等安保服务。 </div> <div> 需满足的要求：具体以采购公告和采购文件为准。 </div> </td> <td style=\"-ms-word-break: break-all;text-align: left\"> 严格落实政府采购相关政策及法律法规。</td> <td align=\"right\" style=\"-ms-word-break: break-all;\">1,486,397.52</td> <td align=\"center\" style=\"-ms-word-break: break-all;\">2025年09月</td> <td style=\"-ms-word-break: break-all; text-align: left\">该项目服务期限为三年。</td> </tr> </table> <br/> <p><i>  本次公开的采购意向是本单位政府采购工作的初步安排，具体采购项目情况以相关采购公告和采购文件为准。</i></p> <P style=\"text-align: right\">汕头市龙湖区大楼服务中心</P> <p style=\"text-align: right\"> 2025年08月06日 </p> </div> </html>

3.	注意事项
1.以上爬取的各项信息若不存在，则赋值为空，以作为缺失值。
2.需要提供所有的数据以及全部爬取代码（要求python），以备核查。
