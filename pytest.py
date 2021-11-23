weight =float(input('น้ำหนักของคุณคือ (กิโลกรัม)  : '))
height =float(input('ส่วนสูงของคุณคือ (เซนติเมตร)  :  '))
bmi = weight / ((height/100)*(height/100))

if bmi <=18.5 :
    print('ค่าดัชนีมวลกายของคุณคือ : {:.2f}'.format(bmi),'=น้ำหนักน้อย')
elif 18.5 < bmi < 25 : 
    print('ค่าดัชนีมวลกายของคุณคือ :{:.2f}'.format(bmi),'=ปกติ')
elif 25 < bmi < 30 :
    print('ค่าดัชนีมวลกายของคุณคือ : {:.2f}'.format(bmi),'=น้ำหนักเกิน')
elif bmi >30 : 
    print('ค่าดัชนีมวลกายของคุณคือ = {:.2f}'.format(bmi),'อ้วน')