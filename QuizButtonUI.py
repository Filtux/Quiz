import PySimpleGUI as sg
import pyautogui
import QuizFunctions as qf


#Base menu options
layout1 = [[sg.Button("Sound")], [sg.Button('Buzzer Select')], [sg.Button('Points')]]

layout2 = [[sg.Button("Add Points")], [sg.Button("Remove Points")]]

#Buzzer Numbers to Add Points
layout3 = [[sg.Button("Home")], [sg.Button("MakeSecondFirst")], [sg.Button("Buzzer 1", key='Add1')], [sg.Button("Buzzer 2", key='Add2')], [sg.Button("Buzzer 3", key='Add3')], [sg.Button("Buzzer 4", key='Add4')], [sg.Button("Buzzer 5", key='Add5')],
[sg.Button("Buzzer 6", key='Add6')], [sg.Button("Buzzer 7", key='Add7')], [sg.Button("Buzzer 8", key='Add8')], [sg.Button("Buzzer 9", key='Add9')], [sg.Button("Buzzer 10", key='Add10')],
[sg.Button("Buzzer 11", key='Add11')], [sg.Button("Buzzer 12", key='Add12')], [sg.Button("Buzzer 13", key='Add13')], [sg.Button("Buzzer 14", key='Add14')], [sg.Button("Buzzer 15", key='Add15')]]

#Buzzer Numbers to Remove Points
layout4 = [[sg.Button("Buzzer 1", key='Rem1')], [sg.Button("Buzzer 2", key='Rem2')], [sg.Button("Buzzer 3", key='Rem3')], [sg.Button("Buzzer 4", key='Rem4')], [sg.Button("Buzzer 5", key='Rem5')],
[sg.Button("Buzzer 6", key='Rem6')], [sg.Button("Buzzer 7", key='Rem7')], [sg.Button("Buzzer 8", key='Rem8')], [sg.Button("Buzzer 9", key='Rem9')], [sg.Button("Buzzer 10", key='Rem10')],
[sg.Button("Buzzer 11", key='Rem11')], [sg.Button("Buzzer 12", key='Rem12')], [sg.Button("Buzzer 13", key='Rem13')], [sg.Button("Buzzer 14", key='Rem14')], [sg.Button("Buzzer 15", key='Rem15')]]

layout = [[sg.Column(layout1, key='MainMenu'), sg.Column(layout2, visible=False, key='RemAddPoints'), sg.Column(layout3, visible=False, key='ChooseBuzzerAdd'), sg.Column(layout4, visible=False, key='ChooseBuzzerRem')]]

buzzerCount = (len(layout3))

print("Items in list equal " + str(buzzerCount))

window = sg.Window("Demo", layout)

while True:
    event, values = window.read()
    print(event, values)

    if event in (None, 'Exit'):
        break

    if event == "Sound":
        qf.clickSound()

    if event == "MakeSecondFirst":
        qf.makeSecondFirst()

    if event == 'Points':
        window[f'MainMenu'].update(visible=False)
        window[f'RemAddPoints'].update(visible=True)

    if event == "Buzzer Select":
        qf.openBuzzerManager()

    if event == "Add Points" :
        window[f'RemAddPoints'].update(visible=False)
        window[f'ChooseBuzzerAdd'].update(visible=True)

    if event == "Remove Points":
        window[f'RemAddPoints'].update(visible=False)
        window[f'ChooseBuzzerRem'].update(visible=True)

    if event == "Home":
        window[f'MainMenu'].update(visible=True)
        window[f'ChooseBuzzerAdd'].update(visible=False)

    if event == "Add1":
        qf.giveTeamPoints(1)
        print("Adding points to " + str(1))

    if event == "Add2":
        qf.giveTeamPoints(2)
        print("Adding points to " + str(2))

    if event == "Add3":
        qf.giveTeamPoints(3)
        print("Adding points to " + str(3))

    if event == "Add4":
        qf.giveTeamPoints(4)
        print("Adding points to " + str(4))

    if event == "Add5":
        qf.giveTeamPoints(5)
        print("Adding points to " + str(5))

    if event == "Add6":
        qf.giveTeamPoints(6)
        print("Adding points to " + str(6))

    if event == "Add7":
        qf.giveTeamPoints(7)
        print("Adding points to " + str(7))

    if event == "Add8":
        qf.giveTeamPoints(8)
        print("Adding points to " + str(8))

    if event == "Add9":
        qf.giveTeamPoints(9)
        print("Adding points to " + str(9))

    if event == "Add10":
        qf.giveTeamPoints(10)
        print("Adding points to " + str(10))

    if event == "Add11":
        qf.giveTeamPoints(11)
        print("Adding points to " + str(11))

    if event == "Add12":
        qf.giveTeamPoints(12)
        print("Adding points to " + str(12))

    if event == "Add13":
        qf.giveTeamPoints(13)
        print("Adding points to " + str(13))

    if event == "Add14":
        qf.giveTeamPoints(14)
        print("Adding points to " + str(14))

    if event == "Add15":
        qf.giveTeamPoints(15)
        print("Adding points to " + str(15))

    if event == "Rem1":
        qf.removeTeamPoints(1)
        print("Removing points from " + str(1))

    if event == "Rem2":
        qf.removeTeamPoints(2)
        print("Removing points from " + str(2))

    if event == "Rem3":
        qf.removeTeamPoints(3)
        print("Removing points from " + str(3))

    if event == "Rem4":
        qf.removeTeamPoints(4)
        print("Removing points from " + str(4))

    if event == "Rem5":
        qf.removeTeamPoints(5)
        print("Removing points from " + str(5))

    if event == "Rem6":
        qf.removeTeamPoints(6)
        print("Removing points from " + str(6))

    if event == "Rem7":
        qf.removeTeamPoints(7)
        print("Removing points from " + str(7))

    if event == "Rem8":
        qf.removeTeamPoints(8)
        print("Removing points from " + str(8))

    if event == "Rem9":
        qf.removeTeamPoints(9)
        print("Removing points from " + str(9))

    if event == "Rem10":
        qf.removeTeamPoints(10)
        print("Removing points from " + str(10))

    if event == "Rem11":
        qf.removeTeamPoints(11)
        print("Removing points from " + str(11))

    if event == "Rem12":
        qf.removeTeamPoints(12)
        print("Removing points from " + str(12))

    if event == "Rem13":
        qf.removeTeamPoints(13)
        print("Removing points from " + str(13))

    if event == "Rem14":
        qf.removeTeamPoints(14)
        print("Removing points from " + str(14))

    if event == "Rem15":
        qf.removeTeamPoints(15)
        print("Removing points from " + str(15))

    if event == 'Buzzer Select':
        window[f'MainMenu'].update(visible=False)
        window[f'ChooseBuzzerAdd'].update(visible=True)

    


window.close()

while True:
    event, values = window.read()
    
    if event == sg.WIN_CLOSED:
        break
window.close()
