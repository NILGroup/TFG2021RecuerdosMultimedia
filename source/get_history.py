from fpdf import FPDF
import os

import utils
import database.daoImage as daoImage
import database.daoQuestion as daoQuestion

class PDF(FPDF):
    def header(self):
        self.image(utils.BOT_WELCOME, 10, 8, 15)
        self.set_font('Helvetica', 'B', 15)
        self.cell(20)
        self.cell(30, 10, 'Remi', 0, 0, 'L')
        self.ln(15)

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.cell(0, 10, 'Página ' + str(self.page_no()), 0, 0, 'C')

def generate_pdf(user_id, user_name, user_lang):
    pdf = PDF()

    pdf.alias_nb_pages()
    pdf.add_page()

    pdf.set_font('Helvetica', 'B', 18)
    pdf.cell(0, 15, 'Questions and answers for user ' + user_name, 0, 1, align="C")

    images = daoImage.get_user_images(user_id)
    image_number = 1

    for num_image in range(len(images)):
        current_image = images[num_image]

        current_questions = daoQuestion.get_image_user_questions(current_image, user_id)

        if len(current_questions) == 0:
            continue

        pdf.set_font('Helvetica', 'B', 16)
        pdf.cell(0, 15, 'Image ' + str(image_number), 0, 1)
        pdf.image(os.path.join(utils.DIR_PATH, "images", "user-images", str(user_id), str(current_image) + 
            ".jpg"), w = 80)        

        for num_questions in range(len(current_questions)):
            current_question = current_questions[num_questions]

            pdf.set_font('Helvetica', 'B', 14)
            pdf.cell(0, 10, current_question[0], 0, 1)
            pdf.set_font('Helvetica', 'I', 12)
            pdf.cell(0, 3, current_question[1], 0, 1,)
            pdf.cell(0, 5, "", 0, 1,)

        image_number += 1

    pdf.output(os.path.join(utils.DIR_PATH, "images", "user-images", str(user_id), "history.pdf"), 'F')