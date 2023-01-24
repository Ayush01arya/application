# importing modules
import time

from PyPDF4 import PdfFileWriter, PdfFileReader
import PyPDF4

from reportlab.pdfgen import canvas
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.lib import colors
from datetime import date
import streamlit as st
# Returns the current local date
st.set_page_config(page_title="GEHU NSS BTL", page_icon='nss-logo.png')
st.info("This Site is only for GEHU NSS UNIT for Bhimtal Campus only",icon="ℹ️")

st.image("GEHU-logo 2.png", width=200)

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        footer {

	visibility: hidden;

	}
footer:after {
	content:'NSS DEV CELL'; 
	visibility: visible;
	display: block;
	position: relative;
	#background-color: red;
	padding: 5px;
	top: 2px;
}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

# st.markdown(hide_streamlit_style, unsafe_allow_html=True)
st.markdown("<h1 style='text-align: center; '>NSS APPLICATION </h1>", unsafe_allow_html=True)
#import streamlit as st

#st.info('This is a purely informational message', icon="ℹ️")
today = date.today()
rt = ['210111558', '220112205', '22011238', '21912061', '210111965', '210121548', '22042547', '22041240', '22031218',
	  '22011461', '21011412',
	  '22041700', '22011540', '220421444',
	  '220112002', '21032521', '220122649', '22151289', '220111918', '220113220', '220112917', '210111825',
	  '22041609', '22032998', '220112002',
	  '22032554', '21012214', '210111457', '22012365', '21042160', '22041950', '22041226', '21042084',
	  '220421290', '210121694', '22011777', '21581104',
	  '22011558', '220111056', '220112077', '220122477', '22581216', '220111968', '220121041', '220411555',
	  '220221217',
	  '22041049', '21031021', '220111267', '220112325', '210111264', '220111964', '22041926', '220112301',
	  '220112242', '22382339', '22022028',
	  '22041926', '21581117', '21581112', '22012642', '220112965', '20141209', '220122662', '22012117',
	  '210111598', '220122267', '220122474',
	  '210111660', '21011397', '21042694', '220121785', '220122561', '22012914', '22031728', '21042224',
	  '22012715', '22011737', '22042354',
	  '22012863', '220112213', '21042013', '21582153', '21011121', '21031407', '22042472', '22031248',
	  '21071014', '21011825', '22041116', '210121548', '22382321',
	  '22031742', '220111373', '22382357', '22031555', '220122513', '220311008', '220123244', '220112441',
	  '21911001', '220112867', '22012425', '21012985',
	  '220122589', '220112238', '226121775', '22041935', '220122589', '220421767', '210121663', '220112489',
	  '220421151', '220121707', '21011179', '21472094',
	  '220111417', '220411160', '220411477', '220421303', '220121701', '21582047', '220122848', '21042151',
	  '22031732', '220121207', '210121141', '21472147',
	  '21582190', '220112605', '21011044', '22041169', '21041263', '22011853', '21042340', '21581076',
	  '22032818', '220122804',
	  '21151046', '20472169', '21912049', '22031939', '22041134', '21582109', '22042286', '22011701',
	  '220112639', '220411094', '22041893',
	  '22011290', '22011975', '22012614', '220112655', '210121901', '220121054', '210111048', '220113098',
	  '22381133', '220112522', '220112748',
	  '22011543', '22012686', '22014925', '220111040', '220411557', '22012814', '21041375', '21582082',
	  '21472101', '22042015', '21581191', '22012904',
	  '220122300', '21032039', '210121108', '21382279', '21582103', '21042136', '220111633', '21712145',
	  '220123223', '220121018', '21011045', '220111512',
	  '22962011', '220112597', '210111706', '210111706', '21032532', '21012681', '21011470', '220121779',
	  '210111538', '21011834', '220411799', '21011848', '21012237',
	  '21032233', '22012275', '220411280', '210111335', '220111976', '22012615', '21011994', '21032040',
	  '21912044', '220121920', '21012925', '220111021', '220121614',
	  '22041169', '21031320', '21011045', '22012567', '20472181', '22012450', '220112669', '220411755',
	  '21472116', '220411249', '22011288''220121920',
	  '220122151', '220113238', '21471010', '22382152', '220122167', '220112321', '21012837', '220122380',
	  '22041786', '22041110', '22041818', '220421291',
	  '21041420', '22011428', '220122775', '220122079', '220111031', '220112040', '220112035', '210121622',
	  '220112867', '22032974', '21032087', '220121858']
student_id=st.text_input("Enter your student ID :- ")
if(student_id in rt):
	st.success("Valid NSS Member ")
	time.sleep(2)
	name = st.text_input("Enter your name :- ")

	course = st.text_input("Enter your course :- ")
	# initializing variables with values
	fileName = 'student_name.pdf'
	documentTitle = 'Request for attendance'
	# title = 'Application'
	# subTitle = 'Application'
	textLines = [
		'To,',
		'The Class Coordinator ',
		'Graphic Era Hill University',
		'Sattal Road,Bhimtal,Uttarakhand 263156',
		'     ',
		f'Date:-{today}',
		'',
		'Subject : Request for attendance',
		'',
		'Respected Sir/Madam,',
		f"With due respect, my name is {name} ,studying in ",
		f"department {course} , holding the ,student id {student_id},",
		"from batch 2021-2025 With humble request I want to state that ",
		"I was participated in NSS events With the ongoing ",
		"preparations, I missed  lecture  and I am going short on ",
		"attendance.Moreover, I bear the responsibility of _____________ .",
		"I request you to kindly allow me the attendance for the ",
		"missed lectures. ",
		"List of events are given below",
		" ",
		" ",
		'Name of the Event                                   Date',
		" ",
		" ",
		" ",
		" ",
		" ",
		" ",
		" ",
		" ",
		" ",
		" ",
		" ",
		" ",
		" ",
		" ",
		" ",
		"Verified By, ",
		" ",
		" ", ]
	textLines2 = [
		"Ayush/Anjali,           Rajendra Singh Bisht    Dr.Sandeep Kumar Budhani",
		"Student Volunteer Head  Asst. Program Officer,  Program Officer,",
		"NSS GEHU,Bhimtal Campus NSS GEHU,Bhimtal Campus NSS GEHU,Bhimtal Campus"

	]

	pdf = canvas.Canvas(fileName)

	pdf.setFillColorRGB(0, 0, 0)
	pdf.setFont("Courier-Bold", 24)

	text = pdf.beginText(25, 790)
	text.setFont("Courier", 15)
	text.setFillColor(colors.black)
	text2 = pdf.beginText(25, 60)
	text2.setFont("Courier", 13)
	text2.setFillColor(colors.black)
	for line in textLines:
		text.textLine(line)
	for line2 in textLines2:
		text2.textLines(line2)
	pdf.drawText(text2)
	pdf.drawText(text)
	pdf.save()
	PyPDF4.PdfFileReader('student_name.pdf')


	def put_watermark(input_pdf, output_pdf, watermark):
		# reads the watermark pdf file through
		# PdfFileReader
		watermark_instance = PdfFileReader(watermark)

		# fetches the respective page of
		# watermark(1st page)
		watermark_page = watermark_instance.getPage(0)

		# reads the input pdf file
		pdf_reader = PdfFileReader(input_pdf)

		# It creates a pdf writer object for the
		# output file
		pdf_writer = PdfFileWriter()

		# iterates through the original pdf to
		# merge watermarks
		for page in range(pdf_reader.getNumPages()):
			page = pdf_reader.getPage(page)

			# will overlay the watermark_page on top
			# of the current page.
			page.mergePage(watermark_page)

			# add that newly merged page to the
			# pdf_writer object.
			pdf_writer.addPage(page)

		with open(output_pdf, 'wb') as out:
			# writes to the respective output_pdf provided
			pdf_writer.write(out)


	if __name__ == "__main__":
		put_watermark(
			input_pdf='NSS.pdf',  # the original pdf
			output_pdf='water.pdf',  # the modified pdf with watermark
			watermark='student_name.pdf'  # the watermark to be provided
		)
	if(student_id and name and course):
		my_bar = st.progress(0)

		for percent_complete in range(100):
			time.sleep(0.1)
			my_bar.progress(percent_complete + 1)

		if(my_bar):
			with open("water.pdf", "rb") as file:
				btn = st.download_button(
					label="Download Your NSS Application",
					data=file,
					file_name=f"NSS{student_id}.pdf",
					mime="application/octet-stream",
					)
		else:
			print("ERR")

		import base64




	else:
		st.info("Loading...")
else:
	st.error("Enter you NSS ID")
