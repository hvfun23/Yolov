if __name__ == "__main__":
    from ultralytics import YOLO

    model = YOLO("yolov8-seg.yaml")

    results = model.train(data=r"C:\Users\acer\PycharmProjects\Skripsi\D2_Mosaic_80\data.yaml",
                          epochs=300, batch=32,  imgsz=640, optimizer="SGD", lr0=0.01) #ubah path dataset