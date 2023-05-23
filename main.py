import user_query
import elastic_work.take_data_from as etd
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from gui_window import Ui_MainWindow


class FindMe(QMainWindow):
    """an application super class to handle with GUI"""
    def __init__(self):
        super(FindMe, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # lists helps to walk throw all components in it to fill and clear
        self.titles = [self.ui.title1, self.ui.title2, self.ui.title3, self.ui.title4, self.ui.title5]
        self.rels = [self.ui.rel1, self.ui.rel2, self.ui.rel3, self.ui.rel4, self.ui.rel5]

        # connect buttons and executable methods
        self.ui.Find.clicked.connect(self.find_butt_clicked)
        for i in range(self.ui.verticalLayout_4.count()):
            self.ui.verticalLayout_4.itemAt(i).widget().clicked.connect(self.view_text)

    def view_text(self):
        """execute when one of the view_button was clicked
            find the document by title and fill the text field with text of doc
        """
        view_but_clc = self.sender()
        # view buttons named by next scheme: button_view{ind}
        # button's and title's indexes are matching
        obj_ind = int(view_but_clc.objectName()[-1])-1
        title = self.titles[obj_ind].text()
        try:
            text = etd.get_doc_by_title(doc_name=title)["_source"]["text"]
        except Exception as e:
            text = f"You tried to find an empty doc and have error: {e}"
        self.ui.FileText.setText(text)

    def set_relevance(self, answ_json):
        """sets the score for each digged document"""
        for i in range(len(answ_json)):
            rel = answ_json[i]["_score"]
            self.rels[i].setText(str(rel))

    def titles_to_titles(self, answ_json):
        """sets the title for each digged document"""
        for i in range(len(answ_json)):
            title = answ_json[i]["_source"]["title"]
            self.titles[i].setText(title)

    def message_box(self, text="Error"):
        """execute an error box with custom text"""
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Critical)
        msg_box.setText(text)
        msg_box.setInformativeText('Close the tab')
        msg_box.setWindowTitle("Message")
        msg_box.exec()

    def clear_out(self):
        """the func is clearing app's output in titles and relevance's labels"""
        for title in self.titles:
            title.setText("")
        for rel in self.rels:
            rel.setText("")

    def find_butt_clicked(self):
        """main function for the app. Connect all other method in it to take user query and convert it to text
            includes error handler for most common user-errors
            clear, parse and set the text
        """
        text_query = self.ui.queryLine.text()
        if not text_query.strip():
            self.message_box("Please, write a query!")
            return
        keys = self.ui.keywordsLine.text().split(",")
        try:
            u_q = user_query.parse_user_sentence(text_query)
        except Exception as e:
            self.message_box(f"Congratulations! You receive an error! {e}")
            return

        u_q["keywords"] = keys
        self.clear_out()
        answer = etd.create_elastic_response(u_q)

        if type(answer) == str:
            self.message_box(answer)
        elif len(answer) == 0:
            self.message_box("We found nothing((")

        self.titles_to_titles(answer)
        self.set_relevance(answer)


# create and open app. Helping sys it could to close without errors
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FindMe()
    window.show()

    sys.exit(app.exec())
