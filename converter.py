import xml.etree.ElementTree as ET
import sqlite3


def convert(*,source, biblename, output):
    root_element = f"""<XMLBIBLE xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" biblename="{biblename}">
 </XMLBIBLE>"""

    connection = sqlite3.connect(source)
    cursor = connection.cursor()
    
    books = dict(cursor.execute("SELECT book_number, long_name FROM books;").fetchall())
    root = ET.fromstring(root_element)

    processed_verses = set()
    processed_chapters = set()
    processed_books = set()

    book_full = cursor.execute("SELECT * FROM verses;").fetchall()

    for book_number, chapter, verse, text in book_full:
        identifier = {
            "book_number": book_number,
            "chapter": chapter,
            "verse": verse,
        }

        if str(book_number) in processed_books:
            book_element = root.find(f'.//BIBLEBOOK[@bnumber="{str(book_number)}"]')
            if f"{book_number}__{chapter}" in processed_chapters:
                chapter_element = book_element.find(f".//CHAPTER[@cnumber='{chapter}']")
                verse_element = ET.Element("VERS")
                verse_element.set("vnumber", str(verse))
                verse_element.text = text
                chapter_element.append(verse_element)
                processed_verses.add(f"{book_number}__{chapter}__{verse}")
            else:
                chapter_element = ET.Element("CHAPTER")
                chapter_element.set("cnumber", str(chapter))
                book_element.append(chapter_element)
                processed_chapters.add(f"{book_number}__{chapter}")
                verse_element = ET.Element("VERS")
                verse_element.set("vnumber", str(verse))
                verse_element.text = text
                chapter_element.append(verse_element)
                processed_verses.add(f"{book_number}__{chapter}__{verse}")
        else:
            book_element = ET.Element("BIBLEBOOK")
            book_element.set("bnumber", str(book_number))
            book_element.set("bname", books[book_number])
            root.append(book_element)
            processed_books.add(str(book_number))
            chapter_element = ET.Element("CHAPTER")
            chapter_element.set("cnumber", str(chapter))
            book_element.append(chapter_element)
            processed_chapters.add(f"{book_number}__{chapter}")
            verse_element = ET.Element("VERS")
            verse_element.set("vnumber", str(verse))
            verse_element.text = text
            chapter_element.append(verse_element)
            processed_verses.add(f"{book_number}__{chapter}__{verse}")

    tree = ET.ElementTree(root)
    tree.write(output, encoding="utf-8", xml_declaration=True)
