#include <stdio.h>
#include <opencv2/opencv.hpp>
#include <opencv2/opencv.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/highgui.hpp>
#include <iostream>
#include <filesystem>

namespace fs = std::filesystem;

using namespace cv;
int main(int argc, char** argv )
{

    // put in loop and do for entire folder
    
    // // Folder where images are located
    // std::string inputFolder = "D:/31-01-23/Desktop/Research/Date_Fruit/Images V2/Images V2/Class 1";
    // std::string outputFolder = "./Class 1";

    // // Create a folder to save images in (will not override if folder exists)
    // if (!fs::exists(outputFolder)) {
    //     fs::create_directory(outputFolder);
    // }

    // Counter to name images
    int i = 1;

    // load image
    Mat raw_img;
    raw_img = imread("D:/31-01-23/Desktop/Research/Date_Fruit/Images V2/Images V2/Class 1/DSC_0001.jpg");
    if ( !raw_img.data )
    {
        printf("No image data \n");
        return -1;
    }

    namedWindow("Display Image", WINDOW_AUTOSIZE );
    imshow("Display Image", raw_img);
    waitKey(500);

    // Resize and Preserve Aspect Ratio
    // scale image
    double scale_down = 0.3;
    Mat scaled_down;
    resize(raw_img,scaled_down, Size(), scale_down, scale_down, INTER_LINEAR);

    namedWindow("Display Image", WINDOW_AUTOSIZE );
    imshow("Display Image", scaled_down);
    waitKey(500);


    // Convert to Gray
    cv::Mat raw_img_gray;
    cv::cvtColor(scaled_down, raw_img_gray, cv::COLOR_BGR2GRAY);

    namedWindow("Display Image", WINDOW_AUTOSIZE );
    imshow("Display Image", raw_img_gray);
    waitKey(500);

    // Erode and Dilate
    cv::Mat kernel = cv::Mat::ones(5, 5, CV_8U);
    cv::Mat erodeGrayImg, dilateImg;
    cv::erode(raw_img_gray, erodeGrayImg, kernel, cv::Point(-1, -1), 3);
    namedWindow("Display Image", WINDOW_AUTOSIZE );
    imshow("Display Image", erodeGrayImg);
    waitKey(500);
    cv::dilate(erodeGrayImg, dilateImg, kernel, cv::Point(-1, -1), 3);
    namedWindow("Display Image", WINDOW_AUTOSIZE );
    imshow("Display Image", dilateImg);
    waitKey(500);

    
    
    // Blur image
    cv::Mat blurrImg;
    cv::GaussianBlur(dilateImg, blurrImg, cv::Size(3, 3), 0);

    namedWindow("Display Image", WINDOW_AUTOSIZE );
    imshow("Display Image", blurrImg);
    waitKey(500);

    // Apply Canny
    cv::Mat imgCanny;
    cv::Canny(blurrImg, imgCanny, 0, 100, 3);

    namedWindow("Display Image", WINDOW_AUTOSIZE );
    imshow("Display Image", imgCanny);
    waitKey(500);

    std::vector<std::vector<Point> > contours;
    std::vector<Vec4i> hierarchy;
    findContours( imgCanny, contours, hierarchy, RETR_TREE, CHAIN_APPROX_SIMPLE );

    RNG rng(12345);
    Mat drawing = Mat::zeros( imgCanny.size(), CV_8UC3 );
     for( size_t i = 0; i< contours.size(); i++ )
        {
        Scalar color = Scalar( rng.uniform(0, 256), rng.uniform(0,256), rng.uniform(0,256) );
        drawContours( drawing, contours, (int)i, color, 2, LINE_8, hierarchy, 0 );
        }

    // Extract coordinates for contour with the largest area
    auto coordinates = *std::max_element(contours.begin(), contours.end(), [](const std::vector<cv::Point>& a, const std::vector<cv::Point>& b) {
        return cv::contourArea(a) < cv::contourArea(b);
    });
    cv::Rect boundingBox = cv::boundingRect(coordinates);

    // Draw bounding box
    cv::rectangle(drawing, boundingBox, cv::Scalar(0, 255, 0), 2);
    namedWindow("Display Image", WINDOW_AUTOSIZE );
    imshow("Display Image", drawing);
    waitKey(0);
    

    // Cropping of raw (resized) img
    int padding = 25;
    int x = std::max(boundingBox.x - padding, 0);
    int y = std::max(boundingBox.y - padding, 0);
    int w = std::min(boundingBox.width + 2 * padding, scaled_down.cols - x);
    int h = std::min(boundingBox.height + 2 * padding, scaled_down.rows - y);
    cv::Mat cropped_img = scaled_down(cv::Rect(x, y, w, h));
    
    namedWindow("Display Image", WINDOW_AUTOSIZE );
    imshow("Display Image", cropped_img);
    waitKey(500);
    return 0;
}