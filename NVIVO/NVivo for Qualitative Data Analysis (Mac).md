# **NVivo for Qualitative Data Analysis (Mac)**

*Siti Lei*  
*Data and Visualization Librarian, Duke Kunshan University*

*Last updated: November 13, 2025*

This 1.5-hour tutorial introduces how to conduct qualitative data analysis using a tool called NVivo in Mac devices, starting from importing qualitative data files, coding, running queries, to analyzing and visualizing codes. We will use a selection of text and image files from the project Data Center Energy Efficiency Focus Groups and Interviews (by U.S. Environmental Protection Agency) and the sample project in NVivo in this tutorial for demonstration. 

[**Before we start	2**](#before-we-start)

[Introduction	2](#introduction)

[About the tool	2](#about-the-tool)

[Setup	3](#setup)

[Datasets	3](#datasets)

[**Before we started	3**](#before-we-started)

[**Create a Project	4**](#create-a-project)

[**Import Files	8**](#import-files)

[Files	8](#files)

[NCapture	10](#ncapture)

[**Text Coding	10**](#text-coding)

[Deductive Coding	10](#deductive-coding)

[Inductive Coding	14](#inductive-coding)

[Mixed Coding	15](#mixed-coding)

[Parent & Child Code	15](#parent-&-child-code)

[Uncoding	19](#uncoding)

[**Highlighter & Coding Stripes	20**](#highlighter-&-coding-stripes)

[**Memos & Annotation	24**](#memos-&-annotation)

[**Image Coding	28**](#image-coding)

[**Save the Project	30**](#save-the-project)

[**Audio & Video Coding	31**](#audio-&-video-coding)

[**Case Classification & Cases	36**](#case-classification-&-cases)

[**Query	41**](#query)

[Word Frequency Query	41](#word-frequency-query)

[Text Search Query	49](#text-search-query)

[Matrix Coding Query	54](#heading=h.h87qgnnc1c3h)

[**Export Codes	61**](#export-codes)

[Code List	61](#code-list)

[Codebook	63](#codebook)

[Individual Code	65](#individual-code)

[**Resources	67**](#resources)

# **Before we start** {#before-we-start}

## **Introduction** {#introduction}

This tutorial is designed for the Mac version of NVivo 14\. If you are using a Windows device, check out [the Windows tutorial here](https://docs.google.com/document/d/1esYrHgOCILlQWpgB5S-ImPCj6XCOwmn4pq6RiV3tD3E/edit?usp=sharing). 

While Lumivero, the company who produces NVivo, has released both Mac and Windows versions, the Mac version currently includes fewer features than the Windows version. Therefore, it is recommended to use a Windows device for working with NVivo. To learn more about the differences between versions and platforms, see the comparison page [here](https://techcenter.qsrinternational.com/Content/nv12/TOC_older_client_versions.htm).

If you don’t have a Windows device, the computers in the Digital Hub in the 4th floor of the DKU Library have installed NVivo 14 (see [Public Devices](https://library.dukekunshan.edu.cn/public-devices/)). 

In the first half of the tutorial, we will work with open datasets(files) from the project [Data Center Energy Efficiency Focus Groups and Interviews](https://catalog.data.gov/dataset/data-center-energy-efficiency-focus-groups-and-interviews), conducted by U.S. Environmental Protection Agency. The raw data was collected between October 2014 and June 2015\. 

For the second half of the tutorial, we will use the sample project in NVivo. Data in this sample project is drawn from a two-year research study (2008-2009) undertaken by researchers from the Duke University Nicholas School of the Environment at the Duke Marine Laboratory in Beaufort, N.C. The study documented community perceptions of development and land-use change on coastal communities in the Down East area of Carteret County, North Carolina, USA.

By the end of this tutorial, you will understand how NVivo can be used in qualitative research​, and use NVivo to load information, code documents and media files, use cases, make notes, conduct queries, and export information.

For questions about the NVivo 14, contact the Data and Visualization Librarian, Siti Lei ([siti.lei@dukekunshan.edu.cn](mailto:siti.lei@dukekunshan.edu.cn)) for support.

## **About the tool** {#about-the-tool}

We will use NVivo 14 in this tutorial. Visit the [Qualitative Data Analysis guide](https://library.dukekunshan.edu.cn/qualitative-data-analysis/) for more information about NVivo.

## **Setup** {#setup}

Follow the instructions in [Downloading, Installing and Licensing NVivo 14](https://library.dukekunshan.edu.cn/qualitative-data-analysis/) to download, install and activate NVivo 14 Mac version on your computer.

## **Datasets** {#datasets}

Download the sample datasets below:

* [Workshop\_Files.zip](https://duke.box.com/s/91jya5x407qpdql8w1mptu70zqb3h00i)

# **Before we started** {#before-we-started}

1. Create a new folder in your computer and name it as **NVivo Workshop**. We will be using this folder to store all the files created in this tutorial.

![][image1]

2. Download the sample dataset [Workshop\_Files.zip](https://duke.box.com/s/91jya5x407qpdql8w1mptu70zqb3h00i).

3. Go to the place where the dataset is saved, right-click on the zip file and select **Quick Look “Workshop\_Files.zip”**.

![][image2]

4. Click on **Uncompress**.

![][image3]

5. Copy or move the unzipped **Workshop\_Files** folder into the **NVivo Workshop** folder. 

![][image4]

# **Create a Project** {#create-a-project}

NVivo projects are saved **locally** on your computer. They are not automatically stored or synced to any cloud space, so remember to back up your files regularly.

1. Go to Launchpad and find NVivo 14\. Double click on the icon to open NVivo 14\.

![][image5]

2. A launch window will appear. Click **Create New Project**.

![][image6]

3. If the window does not appear automatically, hover over the top toolbar. When the menu appears, click **File**, then **New Project**.

![][image7]

4. In the pop-up window, enter **NVivo Workshop** in the “Save As” field, and make sure that the workshop folder is selected as the save location.

![][image8]

5. For the “Project Title” field, enter **NVivo Workshop**.

![][image9]

6. If the data you plan to analyze is not primarily in English, change the **Text Content Language** field accordingly. Then click **Create Project** to continue.

![][image10]

7. When the welcome pop-up appears, click **SKIP TOUR** to close it.

![][image11]

8. The interface of NVivo includes:  
   1) Ribbon  
   2) Navigation View  
   3) List View  
   4) Detail View  
   5) Find Bar  
   6) Quick Coding Bar  
   7) Status Bar

![][image12]  
*Image Source: [The workspace](https://help-nv.qsrinternational.com/14/win/Content/about-nvivo/nvivo-workspace.htm)*

# **Import Files** {#import-files}

NVivo supports organizing files in a hierarchical structure and analyzing a wide range of qualitative data types, including surveys, notes, emails, codebooks, reports, and more.

## **Files** {#files}

1. Go to **Files** under **Data**, right-click on **Files** and select **New Folder…**.

![][image13]

2. In the pop-up, enter **Interview** in the “Name” field, and click **Done**.

![][image14]

3. Make sure the **Interview** under **Files** is selected, then go to the **Import** menu, click on **Files**.

![][image15]

4. In the dropdown, select **Documents…**.

![][image16]

5. In the pop-up window, navigate to the workshop folder, open the Workshop\_Files folder, select all items that begin with “Interview”, and click **Import**.

![][image17]

6. Repeat the same steps for the focus group files. Create a new folder named **Focus Group**, then go to **Import** \> **Files** \> **Documents**. In the Workshop\_Files folder, select all items that begin with “FG”, and click **Import** to continue.

7. The **Interview** and **Focus Group** folders should now appear under **Files**. Double-click each folder to view all the imported documents within it.

![][image18]

8. Hover over the icon next to each file title to see its corresponding file format appears as “Shortcut to \[file format\]”.

![][image19]

## **NCapture** {#ncapture}

If you want to capture content from online sources (e.g., websites, social media posts)and import those into NVivo, **NCapture** is a browser extension that streamlines the process. With NCapture, you can collect online content and import it directly into NVivo. Follow the instructions [here](https://help-nv.qsrinternational.com/20/win/Content/ncapture/ncapture.htm) to install and use NCapture.

# 

# **Text Coding** {#text-coding}

NVivo is a tool not only for qualitative data analysis but also for project management. It supports the entire qualitative research process from collecting and organizing materials to coding, analyzing, visualizing, and sharing results. 

## **Deductive Coding** {#deductive-coding}

Deductive coding is a top-down qualitative analysis approach where you start with a set of predefined codes, and then go through your files, applying those codes to the relevant snippets.

1. To create codes, click **Codes** under **Coding**, then click **Close** to close the introduction page.

![][image20]

2. In the blank area, right-click and select **New Top-Level Code…**.

![][image21]

3. In the pop-up, enter **Energy** in the “Name” field, and click **Done**.

![][image22]

4. Go to **Interview** under **Files**, and double-click to open the **Interview Transcript dec4\_2014 2\_02pm** file.

![][image23]

5. Files imported into NVivo are automatically opened in protected mode, meaning they cannot be edited. To make changes, check **Edit** to turn on editing view.

![][image24]

6. Remember to uncheck it once you’re finished editing.

![][image25]

7. Now, select a text snippet in the **Interview Transcript dec4\_2014 2\_02pm** file, right-click, and select **Code Selection** \> **To Existing Codes or Cases…** from the menu.

![][image26]

8. In the pop-up, select **Imported Products,** and click **Code Selection to ‘Imported Pro…’**.

![][image27]

9. Select another snippet in the same file and right-click to open the content menu. This time, go to **Code Selection** \> **Energy (Codes)**.

![][image28]

10. Alternatively, you can drag and drop the text snippet directly onto the corresponding code in the code list. Let’s try this method with another new snippet.

![][image29]

11. Now, go to **Codes** in the navigation view, you should see the **Energy** code has 1 file and 3 references.

![][image30]

## **Inductive Coding** {#inductive-coding}

Inductive coding is a bottom-up approach where you may want to read through the material first, let ideas and themes emerge naturally, and then create codes based on what you find in the data.

1. In the **Interview dec4\_2014 2\_02pm** file, select one text snippet and right-click, select **Code Selection**, then **To New Code…**.

![][image31]

2. In the pop-up, enter **Cost** in the “Name” field, and click **Done**.

![][image32]

3. Select another snippet in the same file, code it to **Cost**.

4. Go to **Codes** in the navigation view, you should see the **Cost** code has 1 file and 2 references.

![][image33]

## **Mixed Coding** {#mixed-coding}

Mixed coding combines deductive and inductive approaches. For example, you can start coding with some predefined codes and then add new ones as patterns and insights while reading through the data. 

## **Parent & Child Code** {#parent-&-child-code}

Within NVivo, codes can be organized hierarchically by creating parent and child codes.

1. Now, in the **Interview dec4\_2014 2\_02pm** file, select one text snippet and right-click, select **Code Selection**, then **To New Code…**.

![][image34]

2. Enter **Efficiency**, then click the arrow icon.

![][image35]

3. Then, expand **Codes** by clicking on the arrow icon, select **Energy**, and then click **Done**.

![][image36]

4. Repeat the same steps to create another 2 child codes under **Energy**: **Network**, **Air**, and code 2 snippets under each newly created child code.

5. Go to **Codes** in the navigation view. Click on the **\+** icon next to **Energy** \- 3 child codes will appear.

![][image37]

6. Double click on a code, the snippet will show up in the detail view with some quantitative information about each snippet.

![][image38]

7. Now, although the 3 child codes (**Air, Efficiency, Network**) are underneath one parent code (**Energy**), the counts for **Files** and **References** are not aggregated \- this is because NVivo treats parent code and its child codes separately as defaults. 

![][image39]

8. To aggregate them, right-click on **Energy**, then **Get Info**.

![][image40]

9. Check **Aggregate coding from child codes**, and click **Done**.

![][image41]

10. The count of files and references of **Energy** should be updated with the total counts.

![][image42]

## **Uncoding** {#uncoding}

Uncoding means removing a coded snippet from a code that disconnects that piece of data from the theme or category it was assigned to.

1. Double-click on **Chemicals** code \- the snippet of coded text will show up.

![][image43]

2. Select the entire of one snippet, right-click and select **Uncode Selection** \> **From this Code**.

![][image44]

3. The coded text will now be removed. Next, click the hamburger icon, then **Close All** to close all tabs.

![][image45]

# **Highlighter & Coding Stripes** {#highlighter-&-coding-stripes}

The highlighter and coding stripes help visualize and track your coding work in NVivo.

1. Go to **Interview** under **Files**, click on **Interview dec4\_2014 2\_02pm** to open the file.

2. In the detail view, click on the **Highlight** icon, and select **All Coding**.

![][image46]

3. The snippet you’ve coded will be highlighted in yellow.

![][image47]

4. Next, in the detail view, click on the **Coding Stripes** icon, and select **All**.

![][image48]

5. Now, a new pane with multiple colored stripes alongside the file shows which part of the text has been coded and which codes were applied.

![][image49]

6. We can change the color of these bars to visualize our coded content more clearly. To do this, go to **Codes** under **Coding**, select a code and right-click, go to **Color**, then select **Red** as the new color for the code Energy.

![][image50]

7. Repeat the same steps and change the colors of the child codes under the **Energy** code to colors other than red.

8. Now, click the **Coding Stripes** icon again, and make sure **Item Colors** is selected.

![][image51]

9. The color of each code now will appear as the color you selected.

![][image52]

10. Let’s turn off the coding stripes and highlighter by clicking both icons and selecting **None** for now.

![][image53]

# **Memos & Annotation** {#memos-&-annotation}

Memos and annotations help capture your thoughts and insights during analysis. Memos record broader reflections about your data, codes, or project, while annotations act as in-line comments attached to specific text or sections.

1. To create a memo, go to **Interview** under **Files**, right-click on **Interview dec4\_2014 2\_02pm**. Then, select **Link to New Memo…**.

![][image54]

2. Enter **Interview Memo** as the name in the pop-up and click **Done**.

![][image55]

3. A blank page will appear where a detailed memo about the file can be written. For example, noting the interview was conducted in a noisy cafe shop. You can note that here.

![][image56]

4. Once you close the window, the memo is saved and linked to this file. You should see a small icon next to the interview in the list for the memo link when you have the interview list opened completely (with no other files open to the right of it). 

![][image57]

5. To view the memo, right-click on the file again, select **Memo Link** \> **Open Linked Memo**.

![][image58]

6. To create an annotation for a snippet, go to **Interview** under **Files**, double-click on **Interview may13\_2015**.

![][image59]

7. In the detail view, select a text snippet, then select **New Annotation**.

![][image60]

8. A new box will appear next to the selected text. Enter your annotation for this snippet. For example, “This part hasn’t been cleaned yet.”

![][image61]

9. To see memos and annotations you have created all in one place, using the left navigation menu, under **Notes**.

![][image62]

10. Finally, you can also create a note that applies to the entire project. For example, maybe some ideas you have about how the research is going or new themes that are emerging. Double-click on **Memos** under **Notes**. In the detail view, right-click on the blank area and select **New Memo**.

![][image63]

11. Give it a name, such as **Project Memo** and click **Done**.

![][image64]

12. Type some notes, such as “The project needs to be reviewed” and then close it to save. You can always double-click on **Project** from the list of memos to re-open it.

![][image65]

# **Image Coding** {#image-coding}

NVivo allows analyzing visual data by selecting and coding specific areas within an image. You can zoom in, highlight relevant parts of an image, and assign them to existing or new codes, making it possible to integrate visual analysis alongside textual and audio data within the same project.

1. Go to **Focus Group** under **Files** and click on **FG1 Questionnaire 14** to open the PDF file.

![][image66]

2. Note that NVivo 14 does not support **Optical Character Recognition (OCR)**. If your image files contain text that you want to code, make sure they are OCR-processed before importing them into NVivo. For text that cannot be OCRed (like handwriting or signatures), you can manually draw a square around the area you wish to code.

3. Next to **Selection Mode**, select **Region**.

![][image67]

4. Draw a square around the area you want to code, then right-click and select **Code Selection**, then **To Existing Codes or Cases**.

![][image68]

5. Check **Energy**, and click **Select** to continue.

![][image69]

6. Now, go to **Codes** and select **Energy**. In the detail view, instead of showing the image snippet, NVivo will display a screenshot of the selected region. (On Windows, this will appear as the coordinates of the selected image area.)

![][image70]

# **Save the Project** {#save-the-project}

1. Every time when you are done working on editing the project, it is important to remember to save manually. First, hover over the top toolbar and go to the **File** menu.

![][image71]

2. Select **Save** to save the current project.

![][image72]

3. Finally, you can close a project to return to the NVivo main screen. Once your project is saved, go to the **File** menu in the top toolbar and select **Close**.

![][image73]

# **Audio & Video Coding** {#audio-&-video-coding}

NVivo allows the import and analysis of audio and video files through coding specific time segments within those recordings. Please note that the **Transcription** feature in NVivo is not included in our software license; however, transcription can be done using alternative tools such as the **Dictate** feature in Microsoft Word.

1. Go to the **File** menu in the top toolbar and click on **Create Copy of Sample Project**. We will use this sample project for the rest of the workshop.

![][image74]

2. Name the project as its default **Sample Project**. For the saving path, select the workshop folder, and click **Save**.

![][image75]

3. When the welcome pop-up appears, click **SKIP TOUR** to close it.

![][image76]

4. Go to **Files**, then **Interviews** folder. Double click to open the **Betty and Paul** file \- this is a video recording from an interview.

![][image77]

5. Opening this video recording gives us three panels: the audio waveform, the playback window, and a content panel showing timestamps along with the transcript. 

![][image78]

6. Now, go back to the **Interviews** folder, double-click on the **Helen** file \- this is an audio format file. 

![][image79]

7. Like a video format file, the audio recording gives us three panels: the audio waveform, the playback window, and a content panel showing timestamps along with the transcript. 

![][image80]

8. To code the segment, drag the **playhead** in the waveform window to the starting point, then click the **Start Selection** icon at the bottom to begin selecting the segment.

![][image81]

9. When it ends, click the **Finish Selection** icon to complete the coding range.

![][image82]

10. Then, right-click and select **Code Selection**, then **At Existing Codes or Cases**.

![][image83]

11. Select **Memorable quotes** in this case, and click **Select** to confirm.

![][image84]

12. Go to **Codes**, **Memorable quotes**. The timestamp of the segment we just coded will appear.

![][image85]

13. To uncode a segment, click on the segment reference to go back to the source file.

![][image86]

14. From the audio wavement, find the coded segment, right-click and select **Uncode Selection**, then **Memorable quotes (Codes)**.

![][image87]

15. Now the coded segment should be removed.

16. Video coding follows the same steps as audio coding.

# **Case Classification & Cases** {#case-classification-&-cases}

Cases are a special type of code that represents the individuals in your study. If you have demographics or other important attributes that you want to incorporate into your study, case classifications and cases can help. For example, if you were analyzing interview transcripts, you might want to create a case classification called “Person” with attributes such as their name, age, education, job title, etc. Once your case classification is in place that defines what characteristics you want to capture for your interviewees, you could then create one case for each interviewee with those attributes filled in. 

For example, if you interviewed someone named Barbara, you would create a case called BARBARA (or some ID number if needed for confidentiality) with information about Barbara. You would then use that Barbara case to code all the imported content that are associated with Barbara (where the case acts like a code). Later you can then run queries that incorporate that information to answer questions such as, does Barbara talk more about the environment?

You can manually create case classifications and cases by using the left menu, under **Cases**. You can right click on **Case Classification** and **Create a New Classification** or right click on cases to create a new case. But often times, it is easier and more common to upload a spreadsheet with all the information for the cases. We are not going to try that out in this tutorial, but will show you how that would look like.

1. Under **Cases**, go to **Case Classifications**.

![][image88]

2. Double-click to open **Person**, then switch the view from **Attributes** to **Classification Sheet**.

![][image89]

3. A table of all the information about the participants will appear, with different attributes about their background, like the neighborhood they live in, their gender, age range, etc. You can edit the data here.

![][image90]

4. We can take advantage of NVivo’s autocoding features to identify the parts of interviewee and interviewers in a file and code them automatically into the appropriate case. Using the left menu, under **Data**, then **Files**, go to the **Interviews** folder, and open the interview transcript titled “Barbara”. Then, go to **Home** menu \> **Autocode** \> **By Speaker**. You can also right-click on “Barbara” and select **Autocode** \> **By Speaker** to continue.

![][image91]

5. An **Autocode by Speaker** pop-up will appear.

![][image92]

6. The “Barbara” document is formatted in a consistent manner so we can always pick out who is speaking because the person’s name stands on its own line followed by the words they speak. We need to specify who the unique speakers are in this document. In the entering field in the **Autocode by Speaker** pop-up, type in **HENRY** and hit **Enter**. Then type in **BARBARA** and hit the **TAB** key. You should double-check the preview on the right pane to confirm that NVivo is picking up each unique speaker by highlighting them in different colours.

![][image93]

7. Make sure **Cases** is selected for the saving location (**Create cases in** field), and **Person** is selected under **Existing classification**. Then click on **Autocode**. This should code everything that Henry or Barbara said in the transcript with their cases. 

![][image94]

8. Go to **Cases** under **Cases**. 

![][image95]

9. Double click on the **BARBARA** case. You should see everything that Barbara said in her interview. These words are coded to this case. The **BARBARA** case code is now linked to Barbara’s interview responses.

![][image96]

10. Close all the tabs.

# **Query** {#query}

Instead of manually searching through large volumes of coded material, queries in NVivo are powerful tools that help you to quickly grab insight from the data by solving specific questions about your data such as how often certain words/phrases/themes appear, which participants expressed particular attitudes, or how concepts overlap.

This tutorial will not go through all of them in this workshop, but if you are interested in learning more, visit Mac version’s [Queries](https://help-nv.qsrinternational.com/14/mac/Content/queries/queries.htm) page for additional resources. 

## **Word Frequency Query** {#word-frequency-query}

Word frequency query allows you to find the most commonly used words in your sources.

1. First, let’s see how queries can help with making sense of this project. Go to the **Explore** menu to see all available query options.

![][image97]

2. Select **Word Frequency** query, which helps with finding the most frequently used words in the data.

![][image98]

3. Let’s set the search scope limited to the interview script. Next to **Search in**, click on **Selected Items**.

![][image99]

4. In the pop-up, expand **Files**, then click on **Interviews** to select everything in the folder. Next, unselect 2 videos and 1 audio files (with different icons) so that only text transcripts are selected for our search. Click **Select** to continue.

![][image100]

5. The **Finding matches** option helps identify and organize similar or related terms in your text data to varying degrees. Stemmed words means words that share the same root or base form \- for example, talk, talking, talks, and talked all share the stem “talk.” Now, let’s check on **Include stemmed words**, which groups words by the same stem.

![][image101]

6. Set the “Display Words” field to **50**, and keep the “Minimum Word Length” field set to **3**. 

![][image102]

7. Click **Run Query**.

![][image103]

8. Now, we should see the results of our query.

![][image104]

9. Double-click on the word **people**, you will see the location of where the **people** appeared across all of the selected text transcripts.

![][image105]

10. Go back to the first **Unsaved Query**, and you will find out that words like ‘a’, ‘and’, ‘the’ are ignored \- these words are treated as **stop words**, which are those really common words and won’t be useful for analysis. When you see a word in the list and you don’t think they’d be helpful, for example, the word ‘things’, you can right-click on ‘things’ and select **Add to Stop Words List**.

![][image106]

11. To check or reset the stop words list, go to the top toolbar, hover over **Files** and select **Project Properties** from the menu. 

![][image107]

12. Under the **General** tab, you can select text content languages. The default is English (US), but you can switch to other languages. Click on **Stop Words…** to see the current list in use. 

![][image108]

13. From here, you can add stop words manually, or reset the list. But for now, let’s click **Cancel**, then **Cancel** again to close the two pop-ups and return back to the result list.

![][image109]

14. Now let's export the list, since the query results are not saved automatically \- once you close the tab, they will be lost. To save the list as a file on your computer, right-click any word in the list and select **Export**.

![][image110]

15. In the pop-up, give the file a name or keep the default, then browse to the workshop folder. Modify the file format if needed, and click on **Save**.

![][image111]

16. NVivo provides several visualization tools to help you explore your codes. For example, click the **Word Cloud** tab to view our results as a cloud visualization. The Mac version of NVivo offers limited visualization and style options for word frequency queries, whereas the Windows version includes additional visualizations such as Tree Map and Cluster Analysis diagrams.

![][image112]

17. Click **Gallery** to change the appearance of the visualization.

![][image113]

18. Right-click on the visual and select **Export** to save the word cloud in your computer.

![][image114]

19. Close all tabs for now.

![][image115]

## **Text Search Query** {#text-search-query}

Text Search Queries allow you to search for specific words or phrases across your project items.

1. Go to the **Explore** menu and select **Text Search Query**.

![][image116]

2. Keep the search scope as **Files & Externals** \- this includes all imported files in your project. In the search box, enter **water**, and check **Include stemmed words**.

![][image117]

3. Click **Run Query**.

![][image118]

4. A list of files containing the word **water** and its stemmed forms will appear. Double-click **Charles** to view the details.

![][image119]

5. In Charles’s interview transcript, you will see the term **water** highlighted.

![][image120]

6. We can store the results of this query as a new code. To do so, go back to the **Unsaved Query** tab and click **Save Results…**. 

![][image121]

7. In the pop-up, click on the **arrow** icon next to the **Location** field. 

![][image122]

8. Choose **Codes**, then click **Select**.

![][image123]

9. Rename the **Name** field to **Water**, and click **Save Results**.

![][image124]

10. Go to **Codes** in the navigation view. You will see a new code named **Water**, showing the corresponding files and reference counts from the query.

![][image125]

11. If your search phrase contains multiple words, make sure to enclose it in quotation marks (“”). Otherwise, NVivo will treat each word as a separate search term. For example, enter “salt water” in the search box and click **Run Query** again. This new query should return 3 results.  
    * For more tips about building search query, visit [Text Search Query](https://help-nv.qsrinternational.com/14/win/Content/queries/text-search-query.htm) page.

![][image126]

12. Let’s say you want to save this query for future use. To do so, click **Save Criteria…**.

![][image127]

13. Name the query as **Salt Water**, and click **Save Criteria**.

![][image128]

14. Then, close all tabs.

15. Go to **Queries** under **Explore** in the navigation menu. Under **Query Criteria**, you will find **Salt Water** listed. Double-click it to reopen the saved query.

![][image129]

16. Close the tab to continue.

## **Matrix Coding Query**

Matrix Coding Query allows you to compare coding across multiple dimensions, such as codes, cases, or attributes, to identify patterns and relationships in your data. The results are displayed as a matrix table, where rows typically represent cases or participants and columns represent codes or themes. Each cell shows the number of references or the amount of coding coverage where the two dimensions intersect. 

For example, we can look at attitudes expressed by different interviewees based on what they said during the interviews. To run this query, we will use the code “Attitude” and the case “Interview Participants."

1. Go to the **Explore** menu and click **Matrix Coding Query**.

![][image130]

2. Under **Cases**, open **People**. In the list view, click the **\+** icon next to **Interview Participants** to expand the name list.

![][image131]

3. Select all participant names by dragging your cursor over them, then drag the selection into the **Rows** box.

![][image132]

4. Next, under **Codes**, expand **Attitude** by clicking the **\+** icon.

![][image133]

5. Select all items under the **Attitudes** code and drag them into the **Columns** box.

![][image134]

6. Make sure the search scope is set to **Files & Externals**, then click **Run Query**.

![][image135]

7. A matrix table will appear, showing the number of times participants mentioned words related to each attitude.

![][image136]

8. We can color-coded the table to make it more visual. To do that, right-click on the table and go to **Cell Shading**, then **Blue-White**. 

![][image137]

9. Now the table is color-coded — the deeper the color, the higher the count of coded references.

![][image138]

10. We can also visualize other data within this table. To change data sources in the view, right-click anywhere on the table and select **Cell Content** \> **Files Coded** \> **All**. Note that the Windows version offers additional options for displaying data sources, such as words coded, coding presence, and more.

![][image139]

11. This visualization shows the total number of files in which the coded snippet(s) appear.

![][image140]

12. You can export the table by right-clicking the visualization and selecting **Share**. From the available options, choose **Print** to export the visual as a PDF file or **Spreadsheet** to visualize the data using other tools.

![][image141]

13. When finished, close all tabs to return to the main workspace.

# **Export Codes** {#export-codes}

When your analysis is complete, you can export your codes from NVivo in various formats \- as a code list, a codebook, or individual code files.

## **Code List** {#code-list}

1. Go to **Codes** under **Coding,** make sure the list of codes is open and unselected.

2. From the **Share** menu, select **Export** \> **Export List**.

![][image142]

3. Keep the default file name (**Codes**), choose your workshop folder as the save location, and click **OK**.

![][image143]

4. Open the **Codes.docx** file in your workshop folder. You should see a list of all codes displayed in NVivo’s code list.

![][image144]

## **Codebook** {#codebook}

1. Ensure you are in the **Codes** pane and the list of codes is open.

2. From the **Share** menu, select **Export** \> **Export Codebook**.

![][image145]

3. Keep the default file name (**Codebook \- Sample Project**) and make sure MS Word (.docx) is selected as the file format. Click **OK**.

![][image146]

4. Open the **Codebook – Environmental Change Down East.doc** file in your workshop folder. This file displays each code with its description, and the counts of files and references associated with it.

![][image147]

## **Individual Code** {#individual-code}

1. Under **Codes**, select one or more codes to export.

![][image148]

2. From the **Share** menu, select **Export** \> **Export Item**.

![][image149]

3. Make sure the workshop folder is selected, then click **OK**.

![][image150]

4. Each selected code will be saved as a separate file in your workshop folder. For example, opening the **Water** file will display the related reference files, their locations, reference counts, and coverage.

![][image151]

# 

# **Resources** {#resources}

## **Qualitative Research Theory**

* [SAGE Qualitative Research Methods](https://methods.sagepub.com/book/edvol/sage-qualitative-research-methods/toc) \[Online Book\]​  
* [The Essential Guide to Coding Qualitative Data](https://delvetool.com/guide) by Delve​

## **NVivo**

* [NVivo Tutorials](https://lumivero.com/resources/support/getting-started-with-nvivo/nvivo-tutorials/) by Lumivero​  
* [Lumivero Community](https://lumivero.com/resources/support/getting-started-with-nvivo/nvivo-tutorials/) for browsing resources, sharing knowledge, connecting with other NVivo users.​  
* [Transcribe your recordings](https://support.microsoft.com/en-gb/office/transcribe-your-recordings-7fc2efec-245e-45f0-b053-2a97531ecf57) in Microsoft Word​  
* [What is optical character recognition (OCR)?](https://www.ibm.com/think/topics/optical-character-recognition) By IBM

## **Support**

If you have any questions about the tool or this tutorial, don’t hesitate to reach out to the Data and Visualization Librarian, Siti Lei ([siti.lei@dukekunshan.edu.cn](mailto:siti.lei@dukekunshan.edu.cn)) for further support.
