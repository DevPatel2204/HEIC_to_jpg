# HEIC to JPG

A Python tool to convert HEIC images (used by macOS and iOS) to JPG format. Supports both a CLI for batch folder conversion and a Streamlit web UI for drag-and-drop conversion.

---

## Project Structure
```
HEIC_to_png/
├── logic.py   # Core conversion logic (shared)
├── main.py        # CLI script for folder conversion
├── app.py         # Streamlit web UI
└── README.md
```

---

## Requirements

- Python 3.8+
- pip

### Install Dependencies
```bash
pip install pillow pillow-heif streamlit
```

> **macOS note:** If you get a `libheif` error, install it via Homebrew:
> ```bash
> brew install libheif
> ```

---

## Usage

### CLI — Convert a folder of HEIC files
```bash
python main.py <input_folder> <output_folder>
```

- Scans the input folder for `.heic` and `.HEIC` files
- Saves converted `.jpg` files to the output folder
- Creates the output folder automatically if it doesn't exist

---

### Streamlit UI — Browser-based logic
```bash
streamlit run app.py
```

- Opens a local web UI in your browser
- Drag and drop one or multiple HEIC files
- Adjust JPEG quality with a slider (1–95)
- Single file → download as `.jpg`
- Multiple files → download as a `.zip`

---

## Configuration

### JPEG Quality

The default quality is `85`. You can adjust it:

- **CLI:** Edit the `quality` parameter in `main.py`
- **Streamlit:** Use the quality slider in the UI

| Quality | Result |
|---|---|
| 95 | Near lossless, larger file |
| 85 | Default, good balance |
| 60 | Smaller file, noticeable compression |

---

## How It Works

1. `logic.py` registers HEIC support into Pillow via `pillow-heif`
2. Each HEIC file is opened and converted to `RGB` mode (required for JPEG)
3. The image is saved as a `.jpg` file with the specified quality
4. In CLI mode, files are read from and saved to disk
5. In Streamlit mode, files are processed in memory using `io.BytesIO` and returned as downloads

---

## Troubleshooting

| Problem | Fix |
|---|---|
| `UnidentifiedImageError` | Make sure `register_heif_opener()` is called before opening files |
| `libheif not found` | Run `brew install libheif` on macOS |
| No files converted | Check that files end in `.heic` or `.HEIC` |
| `KeyError: 'JPG'` | Use `"JPEG"` not `"JPG"` as the Pillow format string |
| Rotated images | Add `ImageOps.exif_transpose(img)` before saving |

### TESTED ON MACOS (CLI)
