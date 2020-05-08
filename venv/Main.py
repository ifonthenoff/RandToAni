import sys, time, webbrowser, concurrent.futures
import webcrawler, build, accessAnilist

from qtpy import QtWidgets
from ui.mainwindow import Ui_MainWindow
from ui.dialog import Ui_Dialog

animes = dict()
__token = str()
__apiId = 3472

def load():
    global animes
    types = getCheckboxes()
    if not types: return
    animes = webcrawler.crawlList(ui_window.txt_username.text(), types)
    ui_window.textBrowser.clear()

    for key, value in animes.items():
        ui_window.textBrowser.append(key + ": " + str(len(value)) + "\n")

def loadToAni():
    global animes
    failed = []
    total = 0
    count = 0

    if not __token: return
    if not animes: return

    for key, value in animes.items(): total += len(value)
    ui_window.progressBar.setMaximum(total)
    ui_window.progressBar.show()

    starttime = time.time()


    for key, value in animes.items():
        for anime in value:
            thr = accessAnilist.addEntry((anime, key, __token))
            if not thr:
                failed.append(anime)

            print("Anime: " + str(anime.title) + " " + str(anime.score) + " " + str(key))
            print()

            count += 1
            ui_window.progressBar.setValue(count)


        ui_window.textBrowser.clear()

        timePassed = round(time.time() - starttime, 0)
        if timePassed > 60:
            timestring = str(round(timePassed / 60, 0)) + " minutes"
        else:
            timestring = str(timePassed) + " seconds"

        ui_window.textBrowser.append("Time passed: " + timestring)
        ui_window.textBrowser.append("Failed to add the following " + str(len(failed)) + " animes: ")

        for fail in failed:
            ui_window.textBrowser.append(fail.title)
        print("Failed: " + str(len(failed)))

def getCheckboxes() -> list:
    types = []
    if(ui_window.cb_com.isChecked()):
        types.append("completed")
    if(ui_window.cb_cur.isChecked()):
        types.append("currently-watching")
    if(ui_window.cb_dro.isChecked()):
        types.append("dropped")
    if(ui_window.cb_hol.isChecked()):
        types.append("on-hold")
    if(ui_window.cb_pla.isChecked()):
        types.append("plan-to-watch")
    return types

def authorize():
    openBrowser()
    dialog.exec_()

def readToken():
    global __token
    __token = ui_dialog.textBrowser_dialog.toPlainText()
    if __token:
        dialog.close()

def openBrowser():
    url = "https://anilist.co/api/v2/oauth/authorize?client_id={}&response_type=token".format(__apiId)
    print(url)
    webbrowser.open(url)


# initial setup
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QMainWindow()
dialog = QtWidgets.QDialog(window)


# Setup Dialog
ui_dialog = Ui_Dialog()
ui_dialog.setupUi(dialog)

ui_dialog.btn_save.clicked.connect(readToken)
ui_dialog.btn_url.clicked.connect(openBrowser)


# Setup Main Window
ui_window = Ui_MainWindow()
ui_window.setupUi(window)

ui_window.progressBar.hide()
ui_window.btn_load.clicked.connect(load)
ui_window.btn_toAni.clicked.connect(loadToAni)

file = ui_window.menuBar.addMenu("AniList")
file.addAction("Authorize Account")
file.triggered[QtWidgets.QAction].connect(authorize)


# Start Main Window loop
window.show()
sys.exit(app.exec())









