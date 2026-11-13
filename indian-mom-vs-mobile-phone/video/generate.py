from PIL import Image, ImageDraw, ImageFont
from gtts import gTTS
from pathlib import Path
import subprocess, textwrap

BASE = Path(__file__).resolve().parents[1]
OUT = BASE / "output"
OUT.mkdir(exist_ok=True)
W, H, FPS = 1080, 1920, 24
SCENES = [
 {"caption":"रात के 12 बजे… राहुल कंबल में छुपकर गेम खेल रहा है।","dialogue":"राहुल: बस एक आख़िरी गेम! फिर पक्का सो जाऊँगा।","mom":False,"expression":"smile","phone":True},
 {"caption":"मम्मी की आवाज़ सुनते ही राहुल फोन छुपा लेता है।","dialogue":"मम्मी: राहुल! अभी तक जाग रहे हो? राहुल: नहीं मम्मी… मैं तो सो रहा हूँ!","mom":False,"expression":"surprised","phone":True},
 {"caption":"मम्मी कमरे में आती हैं… फोन की चमक सब बता देती है!","dialogue":"मम्मी: अच्छा! तो ये तकिया गेम खेल रहा है? राहुल: अरे… वो…!","mom":True,"expression":"surprised","phone":True},
 {"caption":"मम्मी फोन लेती हैं और खुद रील्स देखने लगती हैं।","dialogue":"राहुल: मम्मी, अब फोन रख भी दो! मम्मी: बस एक आख़िरी रील!","mom":True,"expression":"surprised","phone":True},
 {"caption":"मम्मी गेम जीतकर मुस्कुराती हैं। राहुल हैरान रह जाता है!","dialogue":"राहुल: मेरा फोन वापस दो! मम्मी: पहले तुम सोओ… मैं बॉस लेवल जीतूँ!","mom":True,"expression":"surprised","phone":True},
]
def ft(n,b=False):
 paths=["/usr/share/fonts/truetype/noto/NotoSansDevanagari-Bold.ttf" if b else "/usr/share/fonts/truetype/noto/NotoSansDevanagari-Regular.ttf","/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"]
 for p in paths:
  if Path(p).exists(): return ImageFont.truetype(p,n)
 return ImageFont.load_default()
def center(d,xy,s,f,c):
 d.text(xy,s,font=f,fill=c,anchor="mm",align="center")
def rr(d,xy,r,fill,outline=None,w=4):
 d.rounded_rectangle(xy,radius=r,fill=fill,outline=outline,width=w)
def person(d,x,y,mom=False,expression="smile",phone=False):
 skin="#C98758"
 if mom:
  rr(d,(x-125,y+155,x+125,y+540),48,"#168B55","#0B5635",8)
  d.line((x+65,y+205,x+120,y+510),fill="#E64C4C",width=24)
  d.line((x-110,y+210,x+110,y+210),fill="#E64C4C",width=18)
 else: rr(d,(x-120,y+160,x+120,y+540),50,"#2776D2","#174C91",8)
 rr(d,(x-38,y+115,x+38,y+220),18,skin)
 d.ellipse((x-130,y-35,x+130,y+210),fill=skin,outline="#70432F",width=6)
 if mom:
  d.ellipse((x-145,y-82,x+130,y+78),fill="#17131B")
  d.ellipse((x+75,y-15,x+170,y+95),fill="#17131B")
  d.ellipse((x-12,y+18,x+12,y+43),fill="#D72E39")
 else:
  for dx in (-85,-35,20,70): d.arc((x+dx-25,y-88,x+dx+45,y+25),180,330,fill="#17131B",width=24)
 d.ellipse((x-67,y+55,x-43,y+81),fill="#211A18"); d.ellipse((x+43,y+55,x+67,y+81),fill="#211A18")
 if expression=="surprised": d.ellipse((x-18,y+110,x+18,y+158),fill="#642C25")
 else: d.arc((x-48,y+100,x+48,y+160),5,175,fill="#642C25",width=8)
 if phone:
  rr(d,(x+88,y+245,x+205,y+435),22,"#111827","#E5E7EB",7)
  rr(d,(x+99,y+260,x+194,y+415),13,"#67C7F4")
  center(d,(x+146,y+338),"GAME",ft(22,True),"#17385A")
 center(d,(x,y+585),"मम्मी" if mom else "राहुल",ft(40,True),"white")
def make_scene(i,s):
 im=Image.new("RGB",(W,H),"#18284B"); d=ImageDraw.Draw(im)
 for yy in range(H):
  t=yy/H; d.line((0,yy,W,yy),fill=(int(20+30*t),int(35+25*t),int(72+35*t)))
 rr(d,(60,280,430,690),28,"#263F68","#7899C5",10); d.ellipse((270,340,370,440),fill="#FFE9A6")
 for x,y in [(130,380),(210,540),(340,320)]: d.ellipse((x,y,x+13,y+13),fill="white")
 d.rectangle((0,1450,W,H),fill="#654A45"); rr(d,(65,1250,1015,1760),80,"#245DA8","#A8C9FF",10)
 if s["mom"]:
  person(d,760,780,True,"smile",True); person(d,350,800,False,s["expression"],i<3)
 else: person(d,540,800,False,s["expression"],True)
 if i==0:
  rr(d,(120,1370,960,1660),55,"#2D69BE","#A8C9FF",7); center(d,(540,1510),"कंबल के अंदर…",ft(44,True),"white")
 if i==3: center(d,(760,690),"रील्स!",ft(54,True),"#FFE66D")
 if i==4:
  for x,y in [(180,740),(900,650),(550,630)]: center(d,(x,y),"★",ft(76,True),"#FFE66D")
 rr(d,(42,45,1038,235),38,"#FFF2D0","#F2B94B",7)
 center(d,(540,105),"INDIAN MOM",ft(53,True),"#B12D32"); center(d,(540,178),"VS MOBILE PHONE",ft(53,True),"#1F4F9C")
 rr(d,(55,1635,1025,1795),28,"#FFF7E8","#EABF7A",5)
 center(d,(540,1710),"\n".join(textwrap.wrap(s["caption"],width=30)),ft(34,True),"#252536")
 rr(d,(55,1815,1025,1905),24,"#F7D85B")
 dialog=s["dialogue"] if len(s["dialogue"])<=55 else s["dialogue"][:54]+"…"
 center(d,(540,1860),dialog,ft(28,True),"#302315")
 return im
def ff(args): subprocess.run(["ffmpeg","-hide_banner","-loglevel","error","-y",*map(str,args)],check=True)
def main():
 clips=[]
 for i,s in enumerate(SCENES):
  img=OUT/f"scene_{i+1}.png"; make_scene(i,s).save(img)
  clip=OUT/f"scene_{i+1}.mp4"
  ff(["-loop","1","-i",img,"-t","10","-vf","zoompan=z='min(zoom+0.00025,1.025)':d=240:s=1080x1920:fps=24,format=yuv420p","-r",FPS,"-an","-c:v","libx264","-preset","ultrafast",clip]); clips.append(clip)
 concat=OUT/"concat.txt"; concat.write_text("".join(f"file '{p.name}'\n" for p in clips))
 silent=OUT/"silent.mp4"; ff(["-f","concat","-safe","0","-i",concat,"-c","copy",silent])
 audio=OUT/"hindi_voice.mp3"; gTTS(text=" ".join(s["dialogue"] for s in SCENES),lang="hi").save(str(audio))
 final=OUT/"indian_mom_vs_mobile_phone_50s.mp4"
 ff(["-i",silent,"-i",audio,"-filter_complex","[1:a]apad,atrim=0:50,volume=1.15[a]","-map","0:v","-map","[a]","-t","50","-c:v","copy","-c:a","aac","-b:a","160k","-movflags","+faststart",final])
 print("VIDEO_READY",final)
if __name__=="__main__": main()
