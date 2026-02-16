# Week 4: GUI & Deployment
**Sprint Goal**: Build tkinter interface and finalize app

## Session Outline (2 hours)

### Part 1: GUI Design Principles (15 min)
- User experience basics
- tkinter overview (widgets, layout)
- Show final app demo

### Part 2: Hands-On Coding (75 min)

#### Activity 1: Basic Window (15 min)
**Learning Goal**: Create tkinter window
```python
# Students complete: create_main_window()
# Add title, set size
# Create input fields for 6 key SNPs
```

#### Activity 2: File Upload (20 min)
**Learning Goal**: File dialog integration
```python
# Students complete: upload_csv_button()
# Use filedialog.askopenfilename()
# Parse CSV and populate fields
```

#### Activity 3: Prediction Display (25 min)
**Learning Goal**: Show results dynamically
```python
# Students complete: display_predictions()
# Call predict_all_traits() on button click
# Show results in labels with colors
# Add confidence bars (matplotlib or tkinter Canvas)
```

#### Activity 4: Polish & Test (15 min)
**Learning Goal**: Error handling
```python
# Students add: Input validation
# Handle missing SNPs gracefully
# Add "Clear" and "Export Results" buttons
```

### Part 3: Demo Day (25 min)
- Each student demos their app (2 min each)
- Test with instructor's SNP data
- Peer feedback

### Part 4: Wrap-Up & Next Steps (5 min)
- How to extend: Add more traits (height, lactose intolerance)
- Share on GitHub
- Certificate of completion

## Materials Needed
- `week4_starter.py` template (GUI skeleton)
- `test_snps.csv` (instructor's data)
- Slides: tkinter basics

## Success Criteria
✅ Students create functional GUI  
✅ Students integrate all 3 models  
✅ Students handle file uploads  
✅ Students present working demo

## Bonus Challenges
- Add "Export to PDF" feature
- Create web version with Flask
- Integrate real 23andMe data parser
