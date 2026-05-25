# **Storytelling with ArcGIS StoryMaps**

*Siti Lei*  
*Data and Visualization Librarian, Duke Kunshan University*

*Last updated: March 3, 2026*

This tutorial introduces how to create map-based digital stories with ArcGIS StoryMaps.

**[Before we start](#before-we-start)**

- [Introduction](#introduction)

- [About the tool](#about-the-tool)

- [Datasets](#datasets)

**[Navigate to ArcGIS StoryMaps](#navigate-to-arcgis-storymaps)**

**[Create a StoryMap](#create-a-storymap)**

**[Text Content](#text-content)**

**[Table](#table)**

**[Charts](#charts)**

**[Web Map](#web-map)**

**[Sidecar](#sidecar)**

**[Swipe](#swipe)**

**[Map Tour](#map-tour)**

**[Credits](#credits)**

**[Publish the StoryMap](#publish-the-storymap)**

**[View and Save StoryMap](#view-and-save-storymap)**

**[Resources](#resources)**

# **Before we start**

## **Introduction**

In this tutorial, we will create a map-based digital story that explores airport data across China, building upon the spatial analysis conducted in ArcGIS Online. This demonstration StoryMap transforms spatial data into a clearer picture of national connectivity, presenting the analysis through a structured and engaging narrative format.

Because this tutorial uses the web map and layers developed in the [ArcGIS Online tutorial](https://github.com/itislei/DKU-Library-Data-Visualization-Tutorials/blob/main/ArcGIS/ArcGIS%20Online/ArcGIS%20Online%20for%20Mapping%20Data%20and%20Spatial%20Analysis.md), it is recommended that you complete the ArcGIS Online tutorial before proceeding.

By the end of this tutorial, you will be able to use ArcGIS StoryMaps to design a digital narrative, [Mapping China’s Airports](https://arcg.is/uOT4q), that visualizes geographic distribution and communicates key analytical findings effectively.

## **About the tool**

ArcGIS StoryMaps will be used in the tutorial. Visit the [tool overview](https://www.esri.com/en-us/arcgis/products/arcgis-storymaps/overview) for more information.

## **Dataset**

[ArcGIS Online Demo](https://arcg.is/TqDLG1) (web map) \- Layers from this web map will be used in this tutorial.

Additionally, download the [Sample Dataset.zip](https://github.com/itislei/DKU-Library-Data-Visualization-Tutorials/blob/main/ArcGIS/ArcGIS%20StoryMaps/Sample%20Dataset.zip) file to your local computer. Unzip it and you can find the folder contains the following files:

* **sites** (folder of images)  
* **Captions.docx** (text captions will be used in this tutorial)  
* **Map\_tour\_data.csv** (table exported from the [ArcGIS Online Demo](https://arcg.is/TqDLG1) web map)

# **Navigate to ArcGIS StoryMaps**

1. Sign in to [ArcGIS Online](https://www.arcgis.com/index.html) institutional account. If you are a first time user, follow the instructions in [Signing in to ArcGIS Online](https://library.dukekunshan.edu.cn/signing-in-to-arcgis/).  
2. On the main page, click on the 9-dot (waffle) icon in the upper corner.

<p align="center"><img width="800"  alt="image86" src="https://github.com/user-attachments/assets/25b350d6-09d7-426c-b05c-08d925a9293e" />


3. This will open the menu displaying all add-on products available under our institutional license. From the list, select **StoryMaps**.

<p align="center"><img width="350" alt="image1" src="https://github.com/user-attachments/assets/726dd2ef-cffc-4b70-bf4e-ffddbc2481c1" />


4. Now, you will be directed to ArcGIS StoryMaps.

# **Create a StoryMap**

1. Once you are in the ArcGIS StoryMaps, click on the **\+ Create** button on the upper right corner. Select **Story** from the dropdown list. You will be directed to a new page where you can begin adding and editing content.

<p align="center"><img width="353" height="286" alt="image36" src="https://github.com/user-attachments/assets/34ea56b5-bf62-4095-a72f-b3d316827472" />


2. In the new page, first, enter the story title **"Mapping China's Airports"** into the title field, **"ArcGIS StoryMaps Tutorial"** as the subtitle, and **your name** in the author field.

<p align="center"><img width="520" alt="image84" src="https://github.com/user-attachments/assets/ef8d99c7-9be0-4336-a030-d3034f5fb247" />


3. You may click on the **Change panel appearance** icon to adjust the alignment.

<p align="center"><img width="218" height="196" alt="image69" src="https://github.com/user-attachments/assets/1fa4a529-1aa1-4489-9491-dbb84c9abac6" />


4. Next, click the **Add cover image or video** button in the upper right corner. 

<p align="center"><img width="179" height="59" alt="image81" src="https://github.com/user-attachments/assets/385132d4-535d-4969-b31d-00e220ba59fa" />


5. In the pop-up window, click **Browse your files**.

<p align="center"><img width="478" height="477" alt="image18" src="https://github.com/user-attachments/assets/204e19f8-8ef1-4661-8412-13bab640a2cd" />

6. Navigate to the folder where the site images are stored, select **0\_Airplane\_on\_the\_Runway.jpg**, and click **Open**. 

<p align="center"><img width="700" alt="image95" src="https://github.com/user-attachments/assets/c0969591-c1d2-4de8-9ea4-f6d8dba97c75" />


7. Then click **Add**.

<p align="center"><img width="477" height="475" alt="image67" src="https://github.com/user-attachments/assets/2407c915-7871-4e0a-b610-7c5ce09119e4" />


8. You can adjust the image by clicking the **Options** (Settings) icon, or replace or delete it using the **More actions** (three-dot/ellipsis) icon.

<p align="center"><img width="260" height="139" alt="image35" src="https://github.com/user-attachments/assets/61703ff8-bf6d-4e3e-8aee-8e48884990e4" />


9. ArcGIS StoryMaps includes a variety of pre-made design themes that can be applied directly to your project. For example, click **Design** in the header to explore these options.

<p align="center"><img width="519" height="81" alt="image72" src="https://github.com/user-attachments/assets/ae99d033-c288-4f19-83fa-e0727c33c91e" />


10. The **Design** pane will open, allowing you to customize the appearance of your StoryMap using predefined themes and style elements. In this tutorial, we will use a specific design as an example, but you are welcome to choose the theme that best fits your preference.

<p align="center"><img width="338" height="155" alt="a create storymap 10" src="https://github.com/user-attachments/assets/c5c4f663-4d6c-4b3b-aad4-3574967b14d9" />



11. In this project, change the cover layout to **Side-by-side** and toggle on **Navigation**. We will configure the navigation menu later in the tutorial.

<p align="center"><img width="302" height="352" alt="image28" src="https://github.com/user-attachments/assets/70e9e8ea-3145-489d-91f7-8b785bece058" />


12. For the theme, select **Ridgeline**. You can explore additional options by clicking **Featured themes gallery**.

<p align="center"><img width="306" height="349" alt="a create storymap 12" src="https://github.com/user-attachments/assets/a856fb7e-0dec-475a-9b89-2bd51aa2f648" />


13. Once you have made your selections, close the **Design** pane.  
14. The cover has now been set up. Note that your changes are saved automatically.

<p align="center"><img width="800" alt="a create storymap 14" src="https://github.com/user-attachments/assets/f9a53796-bf17-45e2-b00a-080e6e430fb9" />


# **Text Content**

1. Scroll below the cover to the blank area, click the **\+** button, and select **Text**.

<p align="center"><img width="415" height="402" alt="b text content 1" src="https://github.com/user-attachments/assets/74edf135-65f6-46c1-a4a2-3e10063e0380" />


2. Copy and paste the content under \#1 in captions.docx into the text box. Note that text separated by blank lines will automatically be divided into individual text blocks.

<p align="center"><img width="650" alt="b text content 2" src="https://github.com/user-attachments/assets/c63c9232-cc07-4fc1-b4d9-53d0cc272f86" />


3. Triple click to highlight **“About the Project”**, then switch the font from **Paragraph** to **Heading 1**.

<p align="center"><img width="426" height="235" alt="b text content 3" src="https://github.com/user-attachments/assets/aa022b42-a091-4f1d-8144-daeaa210a35d" />



4. **“About the Project”** is now formatted as a larger, bold heading. It also appears in the navigation menu for easier access.

<p align="center"><img width="650" alt="b text content 4" src="https://github.com/user-attachments/assets/43969dfe-c67d-4bea-8f90-1a17adfc3738" />



5. Next, select the quote below “About the Project”, then switch the font from **Paragraph** to **Quote**.
<p align="center"><img width="650" alt="b text content 5" src="https://github.com/user-attachments/assets/64e6e1db-8afa-490f-9ebd-9d50b8ee6c2a" />


6. Copy and paste the content from section \#2 in captions.docx into the quote source box, then click outside the box to save your changes. Leave the last paragraph in this section as the default text.

<p align="center"><img width="650" alt="b text content 6" src="https://github.com/user-attachments/assets/76add2a4-77b6-4af4-a29d-016b7a6e5965" />



# **Table**

1. Below the content added so far, click the **\+** icon to insert one **separator** and one text asset. Then copy and paste the content from section \#3 in captions.docx into the text box.

<p align="center"><img width="650" alt="c table 1" src="https://github.com/user-attachments/assets/b35e7ba5-b26f-4651-83d2-4985e31a3ccb" />


2. For **“Map 1”,** switch the font from **Paragraph** to **Heading 1**, and for **“Provinces with More Than 10 Airports”**, switch the font from **Paragraph** to **Heading 2**.
<p align="center"><img width="650" alt="c table 2" src="https://github.com/user-attachments/assets/6789ed43-40e8-4f68-9f4d-5850d7925d6f" />



3. Below the text, click the \+ icon and select Table from the list.
   
<p align="center"><img width="650" alt="c table 3" src="https://github.com/user-attachments/assets/8d4d1bab-d8a8-4a80-98dc-371295a3b369" />



4. Copy and paste the table values from section \#4 in captions.docx into the table. Note that importing data from an existing file is not supported, and you cannot paste all content at once. You will need to copy and paste the content into each cell individually.  
5. If you need additional rows or columns, hover along the table edges and click the three-dot (ellipsis) icon. Then select **Insert row below** to add them.

<p align="center"><img width="650" alt="c table 5" src="https://github.com/user-attachments/assets/0b187dd2-3799-4cc4-80c4-5419ddf37b5b" />


6. Lastly, after entering all the data into the table, add a caption below the table using the content from section \#5 in captions.docx.

<p align="center"><img width="650" alt="c table 6" src="https://github.com/user-attachments/assets/08312c21-3ae2-4800-b3ec-0eac53014a9f" />



# **Charts**

1. Continue the Map 1 section, click on the **\+** icon and select **Chart** from the list.

<p align="center"><img width="650" src="https://github.com/user-attachments/assets/be47aeff-f960-4241-849c-3006836ebcc5" />


2. Select **Bar chart** from the options and click **Done**.

<p align="center"><img width="400" alt="image6" src="https://github.com/user-attachments/assets/beda7acd-22a0-4056-b0a5-53f677de71c9" />

3. In the left pane of the new page, copy and paste the content from section \#6 in captions.docx into the table. Note that importing data from an existing file is not supported, and you cannot paste all content at once. You will need to enter the content into each cell individually. Adding multiple columns of data is supported.

<p align="center"><img width="550" alt="charts 3" src="https://github.com/user-attachments/assets/bdcc56b4-bd0b-486e-a7b4-26b041e9f160" />



4. Switch to **Settings** from **Data** tab, copy and paste 

<p align="center"><img width="550" alt="charts 4" src="https://github.com/user-attachments/assets/bc547363-21a0-4117-98e7-c855973dedeb" />



5. Remove the values under **Chart title**, enter **Region of China** in the **Category axis title** field, and **Count of Provinces** in the **Value axis title** field.

<p align="center"><img width="550" alt="charts 5" src="https://github.com/user-attachments/assets/5860737e-3d78-48b4-a1cb-d8a679669780" />



6. Toggle on **Customize axis**, and enter **3** in the field.

<p align="center"><img width="550" alt="charts 6" src="https://github.com/user-attachments/assets/7e496919-1a8c-41b2-9e97-9e35d155705d" />


7. Review the changes and click **Save** to confirm.

<p align="center"><img width="650" alt="charts 7" src="https://github.com/user-attachments/assets/3066d530-dc32-4ee7-9812-a98487035137" />



8. Back to the project, click **Add another block** as we are going to add the donut chart.

<p align="center"><img width="408" height="338" alt="charts 8" src="https://github.com/user-attachments/assets/1032ebbd-79f4-41a6-95db-9b9ae49ebda6" />



9. Select **Donut chart** from the options and click **Done**.
<p align="center"><img width="550" alt="charts 9" src="https://github.com/user-attachments/assets/df90209b-7be7-4730-bfc6-cd32b9bc8c23" />


10. Again, copy and paste the content under \#6 in captions.docx into the table on the left pane of the new page. Note that the donut chart can only work with two data columns.

<p align="center"><img width="550" alt="charts 10" src="https://github.com/user-attachments/assets/b98a8638-6f6f-4243-b0cd-b06c8e70b3bf" />

11. Switch to the **Settings** tab and delete all content in the **Chart title** field.

<p align="center"><img width="550" alt="charts 11" src="https://github.com/user-attachments/assets/07860821-b78e-4a1d-8cd9-d10246525ad4" />


12. Review the chart, then click **Save** when it's ready.

<p align="center"><img width="650" alt="charts 12" src="https://github.com/user-attachments/assets/b77216b1-de99-449c-b9c9-0e0a15ffaa28" />



13. Return to the project, then copy the content from section \#7 in captions.docx and paste it under the charts as the caption. Click anywhere outside the box to save the changes. 

<p align="center"><img width="650"  alt="charts 13" src="https://github.com/user-attachments/assets/f1997403-5553-49e4-8d3f-e59448110b3b" />



14. You may add another chart by clicking the **Add another block** icon, but note that a maximum of three charts is allowed per row.

<p align="center"><img width="650"  alt="charts 14" src="https://github.com/user-attachments/assets/8b836add-5d11-4ee3-b80e-bf79addd8aff" />


# **Web Map**

1. Below the charts, click on the **\+** icon and select **Map** from the list.

<p align="center"><img width="650" alt="d web map 1" src="https://github.com/user-attachments/assets/fdac1698-0658-4fd4-af6b-3d3cb05613fa" />



2. On the new page, if you followed and completed the ArcGIS Online tutorial, you should be able to find your web map project saved under **My Content**. Click on it to continue.

<p align="center"><img width="650" alt="d web map 2" src="https://github.com/user-attachments/assets/26091b17-6cfd-4bff-8fb3-056dd621cddf" />


3. If you do not see it under **My Content**, switch to **My Organization** and search for **ArcGIS Online Demo**. Select the item that matches the search terms exactly.
<p align="center"><img width="650" alt="d web map 3" src="https://github.com/user-attachments/assets/b9354847-0759-4f5c-8944-0759e4885d01" />


4. Under **Layers** tab, make sure that **Count of airports in provinces** and **China Province Boundaries** layers are visible as all others are hidden.  
5. Under **Layers** tab, make sure that **Chinese provinces with other 10 airports** and **China Province Boundaries** layers are visible as all others are hidden.

<p align="center"><img width="550" alt="d web map 5" src="https://github.com/user-attachments/assets/1ef745fd-a973-4b52-9d05-a396627b6a30" />



6. Use the mouse wheel or the **Zoom In** and **Zoom Out** icons at the bottom right corner to adjust the visibility level, then click **Save** to continue.

<p align="center"><img width="650" alt="d web map 6" src="https://github.com/user-attachments/assets/7be6a405-f26d-4d2e-8802-cdf3f365c026" />



7. Back to the project, copy the content from section \#8 in captions.docx and paste it under the map as the caption.

<p align="center"><img width="650" alt="d web map 7" src="https://github.com/user-attachments/assets/b059c260-fa7f-4b0a-93fc-f72fa819c4ee" />


8. Hover over the map, and a toolbar will appear. From there, you can edit the map view, adjust the view window, or remove the map.

<p align="center"><img width="650" alt="d web map 8" src="https://github.com/user-attachments/assets/0689cb21-6195-4883-a96d-2932400af997" />



9. In the next line, click **\+** icon to add a new separator.

<p align="center"><img width="650" alt="d web map 9" src="https://github.com/user-attachments/assets/7eacc5dc-00cd-44cf-8512-30b28daba77c" />



# **Sidecar**

1. Below the web map, click on the **\+** icon and select **Text** from the list.  
2. Copy and paste the content under \#9 in captions.docx into the text box. Change the font style of **“Map 2”** from Paragraph to **Heading 1**, and **“Airport Counts Across All Provinces”** to **Heading 2**.

<p align="center"><img width="650" alt="e sidecar 2" src="https://github.com/user-attachments/assets/f9c22d1d-fd71-4eec-b54c-3d68a852eff7" />


3. Below the text box, click on the **\+** icon and select **Sidecar** from the list.

<p align="center"><img width="450" alt="e sidecar 3" src="https://github.com/user-attachments/assets/ff8ebf75-cd4c-4d40-a78c-ddc4f27a4614" />


4. From the options, select **Floating** and click **Save**.

<p align="center"><img width="450" alt="e sidecar 4" src="https://github.com/user-attachments/assets/7b19283d-c93e-40c0-af27-b21d64aca544" />



5. Under the navigation, click on **\+ Add** button.

<p align="center"><img width="438" height="184" alt="e sidecar 5" src="https://github.com/user-attachments/assets/d0441323-3410-446c-9186-b3bf0462da98" />



6. Select **Map** from the options.

<p align="center"><img width="266" height="530" alt="e sidecar 6" src="https://github.com/user-attachments/assets/dd1e1103-79f2-40c1-99ea-e6818a5eddb7" />


7. On the new page, if you followed and completed the ArcGIS Online tutorial, you should be able to find your web map project saved under **My Content**. Click on it to continue. If you do not see it under **My Content**, switch to **My Organization** and search for **ArcGIS Online Demo**. Select the item that matches the search terms exactly.

<p align="center"><img width="650" alt="e sidecar 7" src="https://github.com/user-attachments/assets/66c55b83-f562-4cb4-bf61-c540a505c5e4" />


8. Under **Layers** tab, make sure that **Count of airports in provinces** and **China Province Boundaries** layers are visible as all others are hidden.

<p align="center"><img width="411" height="346" alt="e sidecar 8" src="https://github.com/user-attachments/assets/76b022a6-4c0a-4c93-9371-7f3b935bc750" />



9. Use the mouse wheel or the **Zoom In** and **Zoom Out** icons at the bottom right corner to adjust the visibility level, then click **Save** to continue.

<p align="center"><img width="650" alt="e sidecar 9" src="https://github.com/user-attachments/assets/cdaa2ea7-4124-4c95-b632-7409d8899675" />


10. You may use the floating toolbar to adjust the map view.

<p align="center"><img width="246" height="106" alt="e sidecar 10" src="https://github.com/user-attachments/assets/bc9a5ffc-d329-4f26-9b78-e024520640fc" />


11. Copy and paste content under \#10 in captions.docx to the left text box.

<p align="center"><img width="550" alt="e sidecar 11" src="https://github.com/user-attachments/assets/de93f9a2-0c4a-4337-b0ad-f94649436ee6" />


12. You may adjust the look of the text. For example, make“higher counts” and “larger and darker” a bold and darker color, while making “fewer airports” and “smaller and lighter” a brighter color.

<p align="center"><img width="518" height="235" alt="e sidecar 12" src="https://github.com/user-attachments/assets/f5d2587c-01a4-4189-947a-f625ff60121d" />


13. Click on the **\+** icon at the bottom right. We are going to add another slide here.

<p align="center"><img width="650"  alt="e sidecar 13" src="https://github.com/user-attachments/assets/98c8f272-cfe0-4ced-a304-6b8aced35f82" />


14. Click on **\+ Add** button and select **Map** from the options. On the new page, open the ArcGIS Online tutorial project either created by yourself under **My Content**, or the one under **My Organization** created by the instructor (if you do not see it under **My Content**, switch to **My Organization** and search for **ArcGIS Online Demo**. Select the item that matches the search terms exactly).   
15. Note that there are two dots that are the smallest and brightest on the map. First, zoom in on the top one.

<p align="center"><img width="650" alt="e sidecar 15" src="https://github.com/user-attachments/assets/9247a46d-2e9b-4b03-af40-3f750a98651a" />


16. Make sure the dot is in the center, then click **Save** to continue.    

<p align="center"><img width="650" alt="e sidecar 16" src="https://github.com/user-attachments/assets/f2608ff2-c67a-4357-9216-a8dec18e72fd" />


17. Copy and paste content under \# 11in captions.docx to the left text box.

<p align="center"><img width="650" alt="e sidecar 17" src="https://github.com/user-attachments/assets/818aa791-eaaf-4977-ad1a-b2718b9746b0" />



18. Repeat the same step and add another slide with the other white dot at the bottom map, along with the corresponding content under \#12 in captions.docx.

<p align="center"><img width="650"  alt="e sidecar 18" src="https://github.com/user-attachments/assets/bd37c71b-7310-4d65-980f-f1ee1ef1ae4e" />


19. Scroll down to the sidecar section below and add a **separator** to continue.

# **Swipe**

1. Below the web map, click the **\+** icon and select **Text** from the list. Copy and paste the content under \#13 in captions.docx into the text box. Then change the font style of **“Map 3”** from **Paragraph** to **Heading 1**, and change **“Airport Locations in Jiangsu Province”** to **Heading 2**.  
2. Below the text, click the **\+** icon and select **Swipe**.

<p align="center"><img width="650" alt="f swipe 2" src="https://github.com/user-attachments/assets/5b2800df-efa7-4594-b5ba-e2bc5afccd68" />


3. First, click on **Add media** on the left pane.

<p align="center"><img width="650" alt="f swipe 3" src="https://github.com/user-attachments/assets/1bac47c9-f75b-4b11-88ef-b439af14dce6" />


4. Select **Web Map** from the options. Note that you can also add an image (e.g., scan of physical map) here.

<p align="center"><img width="275" height="230" alt="f swipe 4" src="https://github.com/user-attachments/assets/85a70a78-2e06-4055-8bc2-ccacc541fb53" />


5. On the new page, again, select the ArcGIS Online tutorial project either created by yourself under **My Content**, or the one under **My Organization** created by the instructor (if you do not see it under **My Content**, switch to **My Organization** and search for **ArcGIS Online Demo**. Select the item that matches the search terms exactly).

6. Under **Layers** tab, make sure that **Airports in Jiangsu** and **China Province Boundaries** layers are visible as all others are hidden.


<p align="center"><img width="404" height="408" alt="f swipe 6" src="https://github.com/user-attachments/assets/f602d675-3e18-4462-b58b-5c5010a57a2c" />


7. Use the mouse wheel or the **Zoom In** and **Zoom Out** icons at the bottom right corner to adjust the visibility level. Make sure Jiangsu Province is centered and clearly visible on the view, then click **Save** to continue.

<p align="center"><img width="650" alt="f swipe 7" src="https://github.com/user-attachments/assets/fd082ece-0857-4c97-909b-cd97a04ffeb3" />



8. Click on **Add web map** at the right pane.

<p align="center"><img width="650"  alt="f swipe 8" src="https://github.com/user-attachments/assets/2ad5ae82-a548-4d10-869e-9ecd15301fd1" />


9. Now, filter to **Living Atlas** and **World**, then pick an option from the result list. For this tutorial, let’s pick up **Open Basemap (Streets)**.

<p align="center"><img width="650" " alt="f swipe 9" src="https://github.com/user-attachments/assets/fe5632b9-f4f3-45c7-999f-36eb6f0a1b8a" />



10. Use the mouse wheel or the **Zoom In** and **Zoom Out** icons at the bottom right corner to adjust the visibility level. Make sure Jiangsu Province is centered and clearly visible on the view, then click **Save** to continue.

<p align="center"><img width="650"  alt="f swipe 10" src="https://github.com/user-attachments/assets/07b1c5b4-4e6d-47b2-958f-f043e129fb58" />



11. If you think the visibility level needs changes, you can always click on the **Edit** icon under each map in the swipe to change it.

<p align="center"><img width="650"  alt="f swipe 11" src="https://github.com/user-attachments/assets/c796fd76-66b7-4003-a5fa-8ce3e34b47e1" />



12. Once you have finished editing the map, drag the **Swipe** icon across the map to compare the layers. You can also use the **Zoom In** and **Zoom Out** icons to adjust the visibility level.

<p align="center"><img width="650" alt="f swipe 12" src="https://github.com/user-attachments/assets/f58bbb2e-ef26-41a9-83b4-935da5d76e93" />



13. Don’t forget to add a caption to the maps. Copy and paste the content under \#14 in the caption file.

<p align="center"><img width="650" alt="f swipe 13" src="https://github.com/user-attachments/assets/4b62416e-cc02-4da0-9abd-f4d02b204f81" />



14. Lastly, hover over the edges of the map and click **Medium** in the floating toolbar. This will enlarge the map view.

<p align="center"><img width="373" height="128" alt="f swipe 14" src="https://github.com/user-attachments/assets/488b7cec-b302-4595-bfda-102122778bf4" />



15. In the new section below, add a **separator** to continue.

# **Map Tour**

1. Below the swipe, click the **\+** icon and select **Text** from the list. Copy and paste the content under \#15 in captions.docx into the text box. Then change the font style of **“Map 4”** from **Paragraph** to **Heading 1**, and change **“Three Closest Airports to DKU”** to **Heading 2**.  
2. Below the text, click the \+ icon and select **Map tour**.

<p align="center"><img width="550" alt="map tour 2" src="https://github.com/user-attachments/assets/4fa78fe7-b34a-4dc9-aaba-f0edce659b25" />


3. From the options, select **Upload photos**.

<p align="center"><img width="650" alt="map tour 3" src="https://github.com/user-attachments/assets/0ea9a264-19bd-4537-bddd-2fdff56973d9" />



4. Click **Browse your files**.

<p align="center"><img width="400" alt="map tour 4" src="https://github.com/user-attachments/assets/58556918-8a50-42f3-8df8-651dc2dc50a8" />



5. Navigate to the sites folder from the sample datasets, and select all image files except 0\_Airport\_on\_Runway, then click **Open**. To select multiple files at once, click the first item, press the **Shift** key on your keyboard, and then click the last item to select all at once.

<p align="center"><img width="650" alt="map tour 5" src="https://github.com/user-attachments/assets/537e68b3-7358-4ba7-a47d-4592b6eddbea" />



6. Make sure 4 images are selected, click **Add**.

<p align="center"><img width="650" alt="map tour 6" src="https://github.com/user-attachments/assets/d1f13605-6995-4177-962a-9485c20847ff" />



7. For the layout, select **List** under **Explorer tour**, and click **Save**.

<p align="center"><img width="650" alt="map tour 7" src="https://github.com/user-attachments/assets/467c6224-faea-44b4-b968-3ade63a4762e" />


8. Copy and paste the content under \#16 in captions.docx as the title and \#17 as the description for the first image into the text box.

<p align="center"><img width="650" alt="map tour 8" src="https://github.com/user-attachments/assets/7fe0c4c9-080e-477e-872c-025e34f5af21" />



9. Next, open **Map\_tour\_data.csv** on your local computer. Drag and select the values under **LAT** and **LNG** for **Duke Kunshan University**.

<p align="center"><img width="650" alt="map tour 9" src="https://github.com/user-attachments/assets/26b4b694-9407-4dd8-b8ed-4dad7c4dfb7b" />



10. Right-click and select **Copy**. Alternatively, press **Ctrl \+ C** on Windows (or **Command \+ C** on Mac) to copy.

<p align="center"><img width="650"  alt="map tour 10" src="https://github.com/user-attachments/assets/d668016c-a64a-4658-ad6d-f885d0cf5216" />



11. Go back to the StoryMap and click **Add location** on the **Duke Kunshan University** card.

<p align="center"><img width="550"  alt="map tour 11" src="https://github.com/user-attachments/assets/b94cc270-9a02-4048-8867-0a2efd70375c" />



12. On the new page, paste the values into the search box in the top-right corner. A dropdown list of matching place names will appear. However, since we are searching by coordinates, press **Enter** to commit the search.

<p align="center"><img width="650" alt="map tour 12" src="https://github.com/user-attachments/assets/f6b34c31-3c43-4a15-adc4-9fae6fb22593" />


13. This will take you to a location near the DKU campus. Zoom out slightly and you will notice the marker is a bit off. Click **Close**, then reselect the correct location. If you are satisfied with the updated location, click **Add to map** to confirm.

<p align="center"><img width="650" alt="map tour 13" src="https://github.com/user-attachments/assets/bd3496d5-546f-4519-81b5-23d856643eb1" />



14. Move your cursor to the center of DKU and click to place a marker.

<p align="center"><img width="650" alt="map tour 14" src="https://github.com/user-attachments/assets/aa82ce9f-cda8-487b-96b8-b47398644e5a" />


15. Set the visibility level to **Use the current zoom level**, then click **Save**.

<p align="center"><img width="400"  alt="map tour 15" src="https://github.com/user-attachments/assets/bf973679-4053-4968-8c76-152017c54a73" />


16. Once editing is complete, switch to the second image from the bottom of the list, or use the mouse wheel to continue making changes.  
17. Repeat steps (\#8–15) to complete the information for the remaining three images.  
18. Then scroll down to the map tour section below and add a **separator** to continue.

# **Credits**

1. In the blank area, create a new text box and copy and paste the content under \#24 in captions.docx into the text box. Change the font style to **Heading 1**.  
2. Then create another text box below. Copy and paste the image source titles under \#25 in captions.docx into this text box.  
3. Select each line of text, click **Link**, and hyperlink the titles using the corresponding URLs listed under \#26 in captions.docx.

<p align="center"><img width="650"  alt="n credits 3" src="https://github.com/user-attachments/assets/8822fd82-306b-4796-8643-1ba334e24e42" />



4. Scroll down to the bottom of the page, and add your self author credits. 

<p align="center"><img width="650"  alt="n credits 4" src="https://github.com/user-attachments/assets/160f220e-834d-4b9b-9396-9ce5a63316f6" />



# **Publish the StoryMap**

1. Once completed the editing, Go to the top menu and click **Publish**.

<p align="center"><img width="500" alt="publish storymap 1" src="https://github.com/user-attachments/assets/90e46183-96a2-40d6-b070-c40d286d91a9" />


2. You may change the title, subtitle, cover by clicking on the **Edit** on the left pane.

<p align="center"><img width="500"  alt="publish storymap 2" src="https://github.com/user-attachments/assets/9b3d8f4d-b968-4564-95c7-25bb49df7f15" />



3. On the right pane, set the sharing level to **Organization**.

<p align="center"><img width="450" alt="publish storymap 3" src="https://github.com/user-attachments/assets/0033cdaa-f098-4062-b00d-9dc64bd592a9" />


4. If you have a group or collaborating with others, you may set the **group sharing**.

<p align="center"><img width="450" alt="publish storymap 4" src="https://github.com/user-attachments/assets/7512f5d3-211e-45b1-ad19-94c903bdd836" />



5. You may also set some advanced options for the sharing, such as allowing others to duplicate or showing your project in the web search results if you set the project to be visible to the public.  
6. When everything is set, click **Publish**.

<p align="center"><img width="400" alt="publish storymap 6" src="https://github.com/user-attachments/assets/f3f85762-a4c1-4e52-ab35-947935314d26" />


7. Now the project should be published. And there are several ways to share it to others and view.

<p align="center"><img width="400"  alt="publish storymap 7" src="https://github.com/user-attachments/assets/d60f57e2-7e3b-48ae-be15-68d93c5913b5" />


# **View and Save StoryMap**

1. After the project is completed, you may click on the View published story button, or copy the link and open in a new tab, or scan the QR code to open. You may also share the link or the QR code.

<p align="center"><img width="450" alt="view and save 1" src="https://github.com/user-attachments/assets/94e40d23-7a49-4a7e-bd85-bd4228b13135" />



2. You can always find the projects or drafts in your [StoryMaps content](https://storymaps.arcgis.com/content).   
3. In the project, you may use the mouse wheel and cursor to scroll through and review the content.  
4. Click the ellipsis (three-dot) icon in the top-right corner to check additional action options.

<p align="center"><img width="550" alt="view and save 4" src="https://github.com/user-attachments/assets/78d39418-98ee-4994-a2ea-5598bd0ea89f" />


5. Note that StoryMaps can be viewed in autoplay mode. To enable this feature, click the ellipsis (three-dot) icon and select **Turn autoplay on**.

<p align="center"><img width="400"  alt="view and save 5" src="https://github.com/user-attachments/assets/37922675-9709-4572-9dea-8352aac8ee4f" />



6. You can also export your project as a PDF by selecting **Print preview** from the same menu.

<p align="center"><img width="400" alt="view and save 6" src="https://github.com/user-attachments/assets/6b8bc44a-4fbe-4636-9f50-37e61091d25a" />


7. Finally, you can save your project as a template by clicking **Save as template**. This allows you to reuse the same layout and assets in the future while simply replacing the content.

<p align="center"><img width="400"  alt="view and save 7" src="https://github.com/user-attachments/assets/03a70e14-3959-4aca-8794-ce5ec0888806" />



# **Resources**

ArcGIS Online offers a wide range of tools for visualizing and analyzing geospatial data, and in this tutorial we’ve only introduced a few. You are encouraged to continue exploring and experimenting with the tool. For further learning, the following resources are recommended:

* [Transferring Data to a Public ArcGIS Account](https://github.com/itislei/DKU-Library-Data-Visualization-Tutorials/blob/main/ArcGIS/Transferring%20Data%20to%20a%20Public%20ArcGIS%20Online%20Account.md), tutorial for long-term preservation for ArcGIS StoryMaps projects  
* [ArcGIS Online Resources](https://www.esri.com/en-us/arcgis/products/arcgis-online/resources) by Esri;  
* [ArcGIS Story Maps Community](https://community.esri.com/t5/arcgis-online/ct-p/arcgis-online), blogs shared by the community;  
* [ArcGIS Story Maps Community Forum](https://community.esri.com/t5/arcgis-storymaps/ct-p/arcgis-storymaps) for asking questions and receiving answers or feedback.

If you have any questions about the tool or this tutorial, don’t hesitate to reach out to the Data and Visualization Librarian, Siti Lei ([siti.lei@dukekunshan.edu.cn](mailto:siti.lei@dukekunshan.edu.cn)) for further support.
