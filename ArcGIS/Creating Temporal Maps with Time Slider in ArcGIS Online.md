# **Creating Temporal Maps with Time Slider**

*Siti Lei*  
*Data and Visualization Librarian, Duke Kunshan University*

*Last updated: April 17, 2026*

This tutorial introduces how to create time-based interactive maps using temporal data in ArcGIS Online.

[**Before we start**](#before-we-start)

[**Introduction**](#introduction)

[**About the tool**](#about-the-tool)

[**Datasets**](#datasets)

[**Sign in to ArcGIS Online**](#heading=h.t4fdu5bc38rs)

[**Import Temporal Data**](#import-temporal-data)

[**Customize Basemap**](#customize-basemap)

[**Visualize Event Data**](#visualize-event-data)

[**Configure Time Setting**](#configure-time-setting)

[**Configure Time Slider**](#configure-time-slider)

[**Resources**](#resources)

# 

# **Before we start** 

## **Introduction** 

This tutorial uses a subset of social events to examine how they spread throughout North America over time.

Tasks covered in this tutorial include:

1. Importing temporal data  
2. Loading and displaying event locations on a map  
3. Configuring time setting  
4. Adjusting animation settings (time range, speed, and playback)

By the end of this tutorial, you will be able to use ArcGIS Online to create an animated map of North America that shows the geographic distribution of events related to the Black Lives Matter movement.

## **About the tool** 

ArcGIS Online will be used in the tutorial. Visit the [GIS guide](https://library.dukekunshan.edu.cn/geographic-information-system-gis/) for more information about the tool.

## **Datasets** 

The sample dataset is sourced from news articles and Wikipedia and has been cleaned for demonstration purposes. Download the sample dataset below:

* BLM\_events.xlsx (Sources are listed under **REFERENCE** column)

## **Import Temporal Data** 

BLM\_events.xlsx is a data table containing information about a selection of social events related to the Black Lives Matter movement, including event names, regions, coordinates, start and end dates, event type, and exposed population. Let's map this data. Before we begin, make sure you have downloaded the file to your computer.

1. Sign in to [ArcGIS Online](https://www.arcgis.com/index.html). If you are a first time user, follow the instructions in [Signing in to ArcGIS Online](https://library.dukekunshan.edu.cn/signing-in-to-arcgis/).

2. Go to **Map** in the header menu.  
3. Once in the map view, go to the left contents toolbar, select **Add**, then **Add layer from file**.

<p align="center"><img width="400" alt="image" src="https://github.com/user-attachments/assets/2812d77a-173d-4eb5-989b-ebb801e15aac" />

4. Click **Your device** button, then select **BLM\_events.xlsx** file (downloaded from the setup files) from its saved location and click **Open**. Alternatively, drag and drop the file into the pop-up window.

<p align="center"><img width="800"alt="image23" src="https://github.com/user-attachments/assets/f9e18fa3-33d8-4899-8ef3-e94ca36ff131" />

5. If you have multiple worksheets in the file, select the one that’s going to be used in this project. If you are using BLM\_events.xlsx dataset, make sure **Example** is selected.

<p align="center"><img width="470"  alt="image" src="https://github.com/user-attachments/assets/19c4dbbb-b6cf-4e57-908e-0a7a9f9dcda2" />

6. Confirm the data type for each variable. Since we are creating a time series map, ensure that the date variables (**DAY\_START** and **DAY\_END**) are set to the **Date** type. In this sample dataset, also verify that **LATITUDE** and **LONGITUDE** are set to **Single** (or **Double**) and that **POPULATION\_EXPOSURE** is set to **Integer**. Click **Next** when ready.

<p align="center"><img width="470" alt="image" src="https://github.com/user-attachments/assets/de178d17-c38c-48b9-85c5-f51c3dd2e8df" />


7. Confirm the location data field again, then click **Next**.

<p align="center"><img width="470"  alt="image" src="https://github.com/user-attachments/assets/d1ee44e6-8c17-420d-a6cd-7ad04b9616f0" />


8. Name this dataset and select the designated folder to save it. Note that the name should be unique across the organization no matter where you save the data. Example: **BLM\_events\_\[Your NetID\]**. Click **Create and add to map**.

<p align="center"><img width="470"  alt="image" src="https://github.com/user-attachments/assets/02447322-f1ba-498b-99fb-45782317fa16" />


9. A map layer with all data points in the dataset will be added to your map\!

<p align="center"><img width="470"  alt="image" src="https://github.com/user-attachments/assets/5a3bf33a-2348-4f33-afbf-a01468776ec3" />


10. Go to **Layers** in the contents toolbar to check the data layer added to the project.

<p align="center"><img width="310" height="125" alt="image" src="https://github.com/user-attachments/assets/ea92edec-8db6-4222-922a-1b0fe339e911" />


## **Customize Basemap** 

1. In the map view, go to **Basemap** in the contents toolbar.

<p align="center"><img width="300" alt="image" src="https://github.com/user-attachments/assets/8d4d71f1-d618-48d8-8939-0d63d19e212a" />


2. Choose **Dark Grey Canvas**.

<p align="center"><img width="300" alt="image" src="https://github.com/user-attachments/assets/3d5b57c2-364b-4edf-bbdc-ea86a1ac08c2" />


3. Click the **close icon** to close the options.

<p align="center"><img width="300" alt="image" src="https://github.com/user-attachments/assets/e6280752-4011-4e6b-a910-e7683b8abfe9" />


4. Go to **Save and open** \> **Save as**.

<p align="center"><img width="300" alt="image" src="https://github.com/user-attachments/assets/88c8bba0-9b4f-4e7a-a5af-916894395008" />


5. Name this map project and select the designated folder to save it. Note that the name should be unique across the organization no matter where you save the project. Example: **Time\_Series\_Map\_\[Your NetID\]**. Click **Save**.

<p align="center"><img width="300" alt="image" src="https://github.com/user-attachments/assets/65c70818-58d7-48ed-86f1-0f801211375d" />


## **Visualize Event Data** 

Since our dataset contains population exposure and event type, let's color-code the points using this data: different colors represent different event types, while the symbol size represents the population exposure count.

1. Make sure the **BLM\_events** layer is selected under **Layers**, then open **Styles** from the right editing toolbar. 

<p align="center"><img width="300" alt="image" src="https://github.com/user-attachments/assets/c3f5d043-36f8-46ac-9ccd-609b9d446d8e" />


2. For **Choose attributes**, click **\+ Field**. 

<p align="center"><img width="300"  alt="image" src="https://github.com/user-attachments/assets/49b4bc63-bbc3-4b0f-89b2-951c769b683c" />


3. Select **EVENT\_TYPE** and **POPULATION\_EXPOSURE** from the menu, then click **Add**.

<p align="center"><img width="300"  alt="image" src="https://github.com/user-attachments/assets/ea28b2ae-0065-49c1-ad0f-70acd9ea206e" />


4. Under Pick a style, choose **Types and size**. You can click the **Styles option** button to further customize the visual elements.

<p align="center"><img width="300"  alt="image" src="https://github.com/user-attachments/assets/69eb4fcc-28c5-4e7d-9831-22c79fbdfee8" />


## **Configure Time Setting** 

Time settings can be configured in the detail view of each map item. To access them, first return to your content.

1. Make sure the map project has been saved, then click the **hamburger (three dashes)icon** in the top-left corner of the page and select **Content**.

<p align="center"><img width="470"  alt="image" src="https://github.com/user-attachments/assets/3a5d5def-e1ba-43a9-b77e-f9dec3a88357" />


2. Locate the BLM\_events map layer, click on the ellipsis (three-dot) icon and go **View details**.

<p align="center"><img width="470"  alt="image" src="https://github.com/user-attachments/assets/1691177f-f580-44b0-b33f-defe1eef2760" />


3. In the layer page, scroll down to **Layers** and click **Example** to expand the item.

<p align="center"><img width="470" alt="image" src="https://github.com/user-attachments/assets/7cd32c8e-0a46-4d69-93c9-79f484db3252" />


4. In the item page, scroll down to **Time settings**, then click **Edit**.

<p align="center"><img width="300"  alt="image" src="https://github.com/user-attachments/assets/8c49a610-1d62-4e02-8975-bbadb4955197" />


5. In the pop up, check **Enable time**. Next, check **time ranges with a start and end time**, and make sure the variables (DAY\_START and DAY\_END) are picked up correctly. Click **OK** to confirm.

<p align="center"><img width="300" alt="image" src="https://github.com/user-attachments/assets/222bdeae-7d22-48c7-99ee-de7ac549098d" />


6. Return to **Content**, click to open the **Time Series Map** project again.  
7. In the detail page, select **Open in Map Viewer**. 

<p align="center"><img width="300"  alt="image" src="https://github.com/user-attachments/assets/1cb30815-065e-40df-b872-94730889ecce" />


8. Now, a time slider will appear in the map.

<p align="center"><img width="470"  alt="image" src="https://github.com/user-attachments/assets/0aac3057-565f-4766-bd48-b2b4655babbe" />


## **Configure Time Slider** 

In ArcGIS Online, you may configure the time range, speed, and playback for your temporal data. 

1. Once the time setting has been configured successfully and the time slider appears in the map view, click the settings icon on the right side of the slider. 

<p align="center"><img width="470" alt="image" src="https://github.com/user-attachments/assets/bb5a6467-e164-4477-b0ec-4057e358b362" />


2. In the pop-up window, explore each tab to adjust how the animation works. For example, to make the animation play faster, go to **Playback rate** and drag the slider all the way to the right to "Fast."

<img width="297" height="213" alt="image" src="https://github.com/user-attachments/assets/2ee55767-2256-4918-8abb-9eebf29022b9" />


3. Make sure you save the project before leaving the page by going to **Save and open \> Save** in the left content toolbar.

<img width="319" height="155" alt="image" src="https://github.com/user-attachments/assets/04b44a28-e1dc-4a4b-a305-1c920eb2a9f0" />


# **Resources** 

ArcGIS Online offers a wide range of tools for visualizing and analyzing geospatial data, and this tutorial only covers some of them. You are encouraged to continue exploring and experimenting with the tool. For further learning, the following resources are recommended:

* [Configure time settings](https://doc.arcgis.com/en/arcgis-online/create-maps/configure-time-mv.htm) by Esri for different map items and their respective time properties;  
* [ArcGIS Online Resources](https://www.esri.com/en-us/arcgis/products/arcgis-online/resources) by Esri;  
* ArcGIS Online [Tool Documentation](https://doc.arcgis.com/en/arcgis-online/analyze/aggregate-points-mv.htm)  
* [ArcGIS Online Community](https://community.esri.com/t5/arcgis-online/ct-p/arcgis-online) for browsing resources, sharing knowledge, and connecting with other users.

If you have any questions about the tool or this tutorial, don’t hesitate to reach out to the Data and Visualization Librarian, Siti Lei ([siti.lei@dukekunshan.edu.cn](mailto:siti.lei@dukekunshan.edu.cn)) for further support.
