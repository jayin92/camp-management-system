from applicant.models import Applicant, Review
import csv, os
from datetime import datetime, timedelta

def get_object(name):
    try:
        return Applicant.objects.get(name=name)
    except Applicant.DoesNotExist:
            return None 
def run():
    script_path = os.path.dirname(__file__)
    rel_path = 'applicant_data.csv'
    abs_path = os.path.join(script_path, rel_path)
    with open(abs_path ,encoding='Big5',newline='') as file:
        early_b = datetime.strptime("2022-12-13 23:59:59", "%Y-%m-%d %H:%M:%S")
        reader = csv.reader(file, delimiter=',')
        next(reader)
        Applicant.objects.all().delete()
        Review.objects.all().delete()
        groupApply = {}
        i = 1
        for row in reader:
            date, time =row[0].split(' ')
            d = datetime.strptime(date,"%m/%d/%Y").strftime("%Y-%m-%d")
            d = datetime.strptime(d, "%Y-%m-%d")
            time = datetime.strptime(time, "%H:%M:%S")
            delta = timedelta(hours=time.hour, minutes=time.minute, seconds=time.second)
            phase_fg = False
            if d+delta <= early_b:
                phase_fg = True       
            cur = Applicant(
                id = i,
                register_time=d+delta,
                email = row[2],
                name = row[3],
                id_number = row[4],
                birthday = datetime.strptime(row[5],'%Y/%m/%d').strftime('%Y-%m-%d'),
                sex = row[6],
                telephone = '0'+row[7] if row[7] != '無' else '',
                parent_phone = '0'+row[8] if row[8] != '無' else '',
                self_phone = '0'+row[9] if row[9] != '無' else '',
                address = row[10],
                emergency_name = row[11],
                emerge_phone = '0'+row[12] if row[12] != '無' else '',
                school = row[13],
                major = row[14],
                club = row[15],
                special_dietary = row[16],
                special_disease = row[17],
                facebook = row[18],
                group_apply = True if row[19] == "是" else False,
                self_introduction = row[23],
                picture = row[24],
                motivation = row[25],
                agreement = row[26],
                sweater_size = row[27],
                want_to_say = row[29],
                phase = 'earlybird' if phase_fg else 'normal',
            )
            if row[20] != '':
                groupApply[cur] = []
                groupApply[cur].append(row[20])
            if row[21] != '':
                groupApply[cur].append(row[21])
            if row[22] != '':
                groupApply[cur].append(row[22])
            i += 1
            cur.save()
        
        for person in groupApply.keys():
            N = person.name
            if N in groupApply[person]:
                groupApply[person].remove(N)
            person.group_person1 = get_object(groupApply[person][0])
            person.group_person2 = get_object(groupApply[person][1])
            if len(groupApply[person]) == 3:
                person.group_person3 = get_object(groupApply[person][2])
            person.save()
        # for person in groupApply.keys():
        #     print(person, groupApply[person])
        file.close()
            
