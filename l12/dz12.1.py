
import codecs
import re

def delete_html_tags(html_file, result_file='cleaned.txt'):
      with codecs.open(html_file, 'r', 'utf-8') as file:
           html = file.read()

      #text without tag
      text_without_tag = re.sub(r'<[^>]*>', '', html)

      #write result
      with codecs.open(result_file, 'w', 'utf-8') as result:
          result.write(text_without_tag)


delete_html_tags('draft.html')

