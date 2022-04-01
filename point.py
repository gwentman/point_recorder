import pickle

print('####################################################')
print('胖大龙积分系统')
print('####################################################')

new_study_point = float(input("Please enter the hour(s) you have studied today: "))
new_workout_point  = float(input("Please enter the hour(s) you have exercised today: "))
new_housework_point = float(input("Please enter the hour(s) you spent on housework today: "))
new_total_point=  new_study_point+new_workout_point+new_housework_point

if new_total_point <= 1:
    print("胖大龙疑似不棒")
else:
    print("胖大龙棒棒棒")
    
try:
    with open("dinosaur_points","rb") as f:
        data = pickle.load(f)
        data['study_point'] += new_study_point
        data['workout_point'] += new_workout_point
        data['housework_point'] += new_housework_point
    with open("dinosaur_points","wb") as f2:
        pickle.dump(data,f2)
    total_point = data['study_point']+data['workout_point']+data['housework_point']
except :
    with open("dinosaur_points","wb") as f:
        data = {"study_point":new_study_point,"workout_point":new_workout_point,"housework_point":new_housework_point}
        pickle.dump(data,f)
        total_point = new_total_point


print('####################################################')
print(f'You currently has a total of {total_point} points')