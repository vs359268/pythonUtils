# -*- coding:utf-8 -*-
# @Time : 2021/3/8 18:46
# @Author: Sun Hao
# @Description: 根据页数切割pdf文件
# @File : pdf_split.py

from PyPDF2 import PdfFileReader, PdfFileWriter

def split_single_pdf(read_file, start_page, end_page, pdf_file):
    #1.获取原始pdf文件
    fp_read_file = open(read_file, 'rb')
    #2.将要分割的pdf内容格式化
    pdf_input = PdfFileReader(fp_read_file)
    #3.实例一个pdf文件编写器
    pdf_output = PdfFileWriter()
    for i in range(start_page, end_page):
        pdf_output.addPage(pdf_input.getPage(i))
    #4.写pdf文件
    with open(pdf_file, 'wb') as pdf_out:
        pdf_output.write(pdf_out)
    print(f'{read_file}分割{start_page}页-{end_page}页完成，保存为{pdf_file}!')


if __name__ == '__main__':
    input_pdf_name = "input.pdf"
    output_pdf_name = 'output.pdf'
    start = 1
    end = 2
    split_single_pdf(input_pdf_name, start, end, output_pdf_name)
