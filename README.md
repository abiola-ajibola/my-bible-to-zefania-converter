# MyBible to Zefania Converter

Convert a **MyBible Android SQLite module** into a **Zefania XML Bible** file.

## Overview

This project provides a command-line script that:

- reads Bible data from a MyBible SQLite database,
- reconstructs the structure as `BIBLEBOOK -> CHAPTER -> VERS`, and
- writes the result as a Zefania-compatible XML document.

## Features

- Converts all books, chapters, and verses from the source database.
- Preserves verse text from the `verses` table.
- Sets Bible version name through a CLI argument (`--biblename`).
- Generates UTF-8 XML with declaration header.

## Installation

This repository currently has no external dependencies.

```bash
git clone https://github.com/abiola-ajibola/my-bible-to-zefania-converter.git
cd my-bible-to-zefania-converter
```

Or run directly with Python.

## Usage

```bash
python main.py --biblename "KJV" --source "/path/to/mybible.SQLite3" --output "./KJV.xml"
```

### CLI Arguments

- `--biblename` (required): Display name for the output Bible in the XML root.
- `--source` (required): Path to the MyBible SQLite database file.
- `--output` (required): Path for the generated Zefania XML file.

## Example

```bash
python main.py \
	--biblename "Yoruba Bible" \
	--source "./data/yoruba.SQLite3" \
	--output "./yoruba-zefania.xml"
```

## Output Structure

The converter generates XML in this shape:

```xml
<?xml version='1.0' encoding='utf-8'?>
<XMLBIBLE biblename="KJV">
	<BIBLEBOOK bnumber="1" bname="Genesis">
		<CHAPTER cnumber="1">
			<VERS vnumber="1">In the beginning...</VERS>
		</CHAPTER>
	</BIBLEBOOK>
</XMLBIBLE>
```

## Notes and Limitations

- The script assumes the source database schema matches MyBible expectations.
- It does not currently validate missing tables/columns before processing.
- It processes all rows from `verses` in database order.

To run help:

```bash
python main.py --help
```
