from wordcloud import WordCloud
import imageio
f=open('Hamlet.TXT','r')
txt=f.read()
f.close()
mask=imageio.imread("13.jpeg")
wordcloud=WordCloud(width=800,height=600,mask=mask).generate(txt)
wordcloud.to_file("1.png")

