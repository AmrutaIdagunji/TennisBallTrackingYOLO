Overview of the Project:
This project focuses on developing an advanced object detection system specifically tailored for tennis. Utilizing a combination of state-of-the-art models including TrackNet, YOLO (You Only Look Once), and OpenCV, the system aims to accurately track tennis balls during matches. This provides a valuable tool for players and coaches, offering detailed game analysis and insights that were previously available only with high-end, expensive professional sports technologies.

1. Before executing the scripts. Download the annotated datasets for training.

2. Once the dataset is ready, make sure the paths are updated in all the scripts, wherever necessary.

3. Note that the data we downloaded followed this hierarchy.
Dataset/
├── Readme.docx
├── game1/
│     ├── Clip1/
│     │     ├── 0000.jpg
│     │     ├── 0001.jpg
│     │     ├── …
│     │     └── Label.csv
│     ├── Clip2/
│     │     ├── 0000.jpg
│     │     ├── 0001.jpg
│     │     ├── …
│     │     └── Label.csv
│     ├── 
│     │ ⋮
│     └── 
├── game2/
├── ...
└── game10/

4. You may have to change the preprocessing code based on the paths. (multiple for loops used to traverse this folder structure)

5. First Principles: run "opencvHoughTransformImage.py" to test if HoughCircles can detect the balls
6. Using CNN: run the "game-analysis-with-custom-cnn.ipynb" file, which contains the code for both multi-class classification and multi-label regression.
7. YOLO: "game-data-with-yolo.ipynb" file contains the code to preprocess the data, create text files with bounding box co-ordinates, fetch and install YOLO. Then it trains the model on your training set. Then, use the weights to predict the ball.

