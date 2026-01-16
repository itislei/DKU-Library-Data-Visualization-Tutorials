# **NVivo for Qualitative Data Analysis (Windows)**

*Siti Lei*  
*Data and Visualization Librarian, Duke Kunshan University*

*Last updated: November 11, 2025*

This 1.5-hour tutorial introduces how to conduct qualitative data analysis using a tool called NVivo in Windows devices, starting from importing qualitative data files, coding, running queries, to analyzing and visualizing codes. We will use a selection of text and image files from the project Data Center Energy Efficiency Focus Groups and Interviews (by U.S. Environmental Protection Agency) and the sample project in NVivo in this tutorial for demonstration. 

[**Before we start	2**](#before-we-start)

[Introduction	2](#introduction)

[About the tool	2](#about-the-tool)

[Setup	3](#setup)

[Datasets	3](#datasets)

[**Before we started	3**](#before-we-started)

[**Create a Project	5**](#create-a-project)

[**Import Files	8**](#import-files)

[Files	8](#files)

[NCapture	10](#ncapture)

[**Text Coding	10**](#text-coding)

[Deductive Coding	10](#deductive-coding)

[Inductive Coding	14](#inductive-coding)

[Mixed Coding	16](#mixed-coding)

[Parent & Child Code	16](#parent-&-child-code)

[Uncoding	20](#uncoding)

[**Highlighter & Coding Stripes	21**](#highlighter-&-coding-stripes)

[**Memos & Annotation	24**](#memos-&-annotation)

[**Image Coding	29**](#image-coding)

[**Save the Project	30**](#save-the-project)

[**Audio & Video Coding	32**](#audio-&-video-coding)

[**Case Classification & Cases	36**](#case-classification-&-cases)

[**Query	41**](#query)

[Word Frequency Query	42](#word-frequency-query)

[Text Search Query	52](#text-search-query)

[Matrix Coding Query	57](#matrix-coding-query)

[**Export Codes	64**](#export-codes)

[Code List	64](#code-list)

[Codebook	66](#codebook)

[Individual Code	67](#individual-code)

[**Resources	69**](#resources)

# 

# **Before we start** {#before-we-start}

## **Introduction** {#introduction}

This tutorial is designed for the Windows version of NVivo 14\. If you are using a Mac device, check out here (coming soon). 

While Lumivero, the company who produces NVivo, has also released a Mac version, it currently includes fewer features than the Windows version. Therefore, it is recommended to use a Windows device for working with NVivo. To learn more about the differences between versions and platforms, see the comparison page [here](https://techcenter.qsrinternational.com/Content/nv12/TOC_older_client_versions.htm).

If you don’t have a device, the Windows computers in the Digital Hub in the 4th floor of the DKU Library have installed NVivo 14 (see [Public Devices](https://library.dukekunshan.edu.cn/public-devices/)). 

In the first half of the tutorial, we will work with open datasets(files) from the project [Data Center Energy Efficiency Focus Groups and Interviews](https://catalog.data.gov/dataset/data-center-energy-efficiency-focus-groups-and-interviews), conducted by U.S. Environmental Protection Agency. The raw data was collected between October 2014 and June 2015\. 

For the second half of the tutorial, we will use the sample project in NVivo. Data in this sample project is drawn from a two-year research study (2008-2009) undertaken by researchers from the Duke University Nicholas School of the Environment at the Duke Marine Laboratory in Beaufort, N.C. The study documented community perceptions of development and land-use change on coastal communities in the Down East area of Carteret County, North Carolina, USA.

By the end of this tutorial, you will understand how NVivo can be used in qualitative research​, and use NVivo to load information, code documents and media files, use cases, make notes, conduct queries, and export information.

For any questions about the NVivo 14, contact the Data and Visualization Librarian, Siti Lei ([siti.lei@dukekunshan.edu.cn](mailto:siti.lei@dukekunshan.edu.cn)) for support. 

## **About the tool** {#about-the-tool}

We will use NVivo 14 in this tutorial. Visit the [Qualitative Data Analysis guide](https://library.dukekunshan.edu.cn/qualitative-data-analysis/) for more information about NVivo.

## **Setup** {#setup}

Follow the instructions in [Downloading, Installing and Licensing NVivo 14](https://library.dukekunshan.edu.cn/qualitative-data-analysis/) to download the NVivo 14 Windows version on your computer.

## **Datasets** {#datasets}

Download the sample datasets: [Workshop\_Files.zip](https://duke.box.com/s/91jya5x407qpdql8w1mptu70zqb3h00i)

# **Before we started** {#before-we-started}

1. Create a new folder in your computer and name it as **NVivo Workshop**.

![][image1]

2. Download the sample dataset [Workshop\_Files.zip](https://duke.box.com/s/91jya5x407qpdql8w1mptu70zqb3h00i).

3. Unzip the file by right-clicking and select **Extra All**. Select where the files are extracted.

![][image2]

4. Click on **Browse** if you need to adjust the saving path. Once it’s finished, click **Extract**.  
   * Alternatively, you might first install a great little program called [7-Zip](https://www.7-zip.org/) \-  that is helpful to use when working with zip files. Then you should be able to right-click on the zip file and select **7-Zip**, then **Extract** **Here** to extract its files

![][image3]

5. Copy or move the unzipped sample data folder into the **NVivo Workshop** folder. 

![][image4]

# **Create a Project** {#create-a-project}

NVivo projects are saved **locally** on your computer. They are not automatically stored or synced to any cloud space, so remember to back up your files regularly.

1. Open NVivo 14 on your desktop. Then, click on **\+ New Project**. Note that NVivo runs locally in your device, so you don’t have to login to your NVivo account to use the software.

![][image5]

2. First, enter **NVivo Workshop** as the project title.

3. Click **Browse…** to choose where the project file will be saved. Select the **NVivo Workshop** folder we created in the previous section.

4. If the content you plan to analyze is not primarily in English, change the **Text content language** accordingly. Then click **Next** to continue.

![][image6]

5. In the next pop-up window, review or adjust your saving options as needed, then click **Create Project** to continue.

![][image7]

6. When the welcome pop-up appears, click **SKIP TOUR** to close it.

![][image8]

7. The interface of NVivo includes:  
   1) Ribbon  
   2) Navigation View  
   3) List View  
   4) Detail View  
   5) Find Bar  
   6) Quick Coding Bar  
   7) Status Bar

![][image9]  
*Image Source: [The workspace](https://help-nv.qsrinternational.com/14/win/Content/about-nvivo/nvivo-workspace.htm)*

# **Import Files** {#import-files}

NVivo supports the analysis of various qualitative data file types, including surveys, notes, emails, codebooks, reports, and more. 

## **Files** {#files}

1. Go to **Files** under **Data**, right-click on **Files** and select **New Folder…**.

![][image10]

2. In the pop-up, enter **Interview** in the “Name” field, and click **OK**.

![][image11]

3. Make sure the **Interview** under **Files** is selected, then go to the **Import** menu, click on **Files**.

![][image12]

4. Under ‘File Type’, make sure **Support Files** is selected.

![][image13]

5. In the pop-up window, navigate to the workshop folder, open the Workshop\_Files folder, select all items that begin with “Interview”, and click **Import**.

![][image14]

6. Repeat the same steps for the focus group files. Create a new folder named **Focus Group**, then go to **Import** \> **Files** \> **Documents**. In the Workshop\_Files folder, select all items that begin with “FG”, and click **Import** to continue.

7. The **Interview** and **Focus Group** folders should now appear under **Files**. Double-click each folder to view all the imported documents within it.

![][image15]

## **NCapture** {#ncapture}

**NCapture** is a browser extension that allows collecting web and social media content for import into NVivo for qualitative analysis. Follow the instructions [here](https://help-nv.qsrinternational.com/20/win/Content/ncapture/ncapture.htm) to install and use NCapture, and to import captured files into NVivo.

# **Text Coding** {#text-coding}

NVivo is a tool not only for qualitative data analysis but also for project management. It supports the entire qualitative research process from collecting and organizing materials to coding, analyzing, visualizing, and sharing results. 

While NVivo offers features such as auto-coding and visualization, researchers still **lead** the analysis and interpretation; NVivo is an assistive tool, not an automated one.

## **Deductive Coding** {#deductive-coding}

Deductive coding is a top-down qualitative analysis approach where you start with a set of predefined codes, and then go through your files, applying those codes to the relevant snippets.

1. To create codes, click **Codes** under **Coding**, then click **Close** to close the introduction page.

![][image16]

2. Right-click on **Codes** under **Coding**, select **New Code…** from the menu.

![][image17]

3. Enter **Energy** in the ‘Name’ field, then click **OK**. Our first code **Energy** is now created.

![][image18]

4. Now, go to **Interview** under the **Files**. Double-click on **Interview dec4\_2014 2\_02pm** to open the file located at the top.

![][image19]

5. Files imported into NVivo are automatically opened in protected mode, meaning they cannot be edited. To make changes, select **Edit** to turn on editing view.

![][image20]

6. Remember to uncheck it once you’re finished.

![][image21]

7. Now, select a text snippet in the **Interview dec4\_2014 2\_02pm** file right-click, and select **Code Selection** from the menu.

![][image22]

8. In the pop-up, select **Energy,** and click **Code Selection to ‘Energy’**.

![][image23]

9. Select another snippet in the same file and right-click to open the content menu. This time, go to **Code to Recent Codes** \> **Energy**.

![][image24]

10. Alternatively, if you have the **Codes** open in the navigation view, you can drag and drop the text snippet directly onto the corresponding code. Let’s try this method with another new snippet.

![][image25]

11. Go to **Codes** in the navigation view, you should see the **Imported Products** code has 1 file and 3 references.

![][image26]

## **Inductive Coding** {#inductive-coding}

Inductive coding is a bottom-up approach where you may want to read through the material first, let ideas and themes emerge naturally, and then create codes based on what you find in the data.

1. In the **Interview dec4\_2014 2\_02pm** file, select one text snippet and right-click, select **Code Selection…** from the menu.

![][image27]

2. Go to **Top-Level Code** under **Create New**.

![][image28]

3. Enter **Cost** as the new code, and click **Code Selection to ‘Cost’**.

![][image29]

4. Select another snippet in the same file, code it to **Cost**.

5. Go to **Codes** in the navigation view, see the **Cost** code has 1 file and 2 references.

![][image30]

## **Mixed Coding** {#mixed-coding}

Mixed coding combines deductive and inductive approaches. For example, you can start coding with some predefined codes and then add new ones as patterns and insights while reading through the data. 

## **Parent & Child Code** {#parent-&-child-code}

Within NVivo, codes can be organized hierarchically by creating parent and child codes.

1. Go to **Interview** under **Files**, click on **Interview dec4\_2014 2\_02pm** to open the file.

2. Now, select a text snippet and right-click, select **Code Selection…** from the menu.

![][image31]

3. Select **Energy**, then click on **Child Code** on the right pane.

![][image32]

4. Enter **Efficiency** as the new code, then click **Code Selection to ‘Efficiency’**.

![][image33]

5. Repeat the same steps to create another 2 child codes under **Energy**: **Network**, **Air**, and code 2 snippets under each newly created child code.

6. Go to **Codes** in the navigation view. Click on the **\+** icon next to **Energy** \- 3 child codes will appear.

![][image34]

7. Double click on a code, the snippet will show up in the detail view with some quantitative information about each snippet.

![][image35]

8. Now, although the 3 child codes (**Air**, **Efficiency**, **Network**) are underneath one parent code (**Energy**), the counts for **Files** and **References** are not aggregated \- this is because NVivo treats parent code and its child codes separately as defaults. 

![][image36]

9. To aggregate them, right-click on **Energy**, then **Code Properties**.

![][image37]

10. Check **Aggregate coding from children**, and click **OK**.

![][image38]

11. The count of files and references of **Energy** should be updated with the total counts.

![][image39]

## **Uncoding** {#uncoding}

Uncoding means removing a coded snippet from a code that disconnects that piece of data from the theme or category it was assigned to.

1. Double-click on **Network** code \- the snippet of coded text will show up.

![][image40]

2. Select the entire of one snippets, right-click, then select **Uncode From This Code**.

![][image41]

3. The coded text will now be removed. Next, click the **×** on each of the file title tabs to close all open windows.

![][image42]

# **Highlighter & Coding Stripes** {#highlighter-&-coding-stripes}

The highlighter and coding stripes help visualize and track your coding work in NVivo.

1. Go to **Interview** under **Files**, double-click on **Interview dec4\_2014 2\_02pm** to open the document.

2. In the detail view, click on the highlighter icon, and select **All Coding**.

![][image43]

3. The snippet you’ve coded will be highlighted in yellow.

![][image44]

4. In the detail view, click on the coding stripes icon, and select **All**.

![][image45]

5. Now, a new pane with multiple colored bars alongside the file shows which part of the text has been coded and which codes were applied.

![][image46]

6. To change the color of each code, go to **Codes** under **Coding**, select **Energy** code and right-click, go **Color**, and select **Red** as the new color.

![][image47]

7. Repeat the same steps and change the colors of the Cost code to a color other than red.

8. Now, click the coding stripes icon again, and select **Item Colors**.

![][image48]

9. The color of each code now will appear as the color you selected.

![][image49]

10. Let’s turn off the coding stripes and highlighter by clicking both icons and selecting **None** for now, and close the **Interview dec4\_2014 2\_02pm** file.

![][image50]

# **Memos & Annotation** {#memos-&-annotation}

Memos and annotations help capture your thoughts and insights during analysis. Memos record broader reflections about your data, codes, or project, while annotations act as in-line comments attached to specific text or sections.

1. To create a memo, go to **Interview** under **Files**, right-click on **Interview dec4\_2014 2\_02pm**. Then, **select Link to New Memo…**.

![][image51]

2. Enter **Interview Memo** as the name and click **OK**.

![][image52]

3. A blank page will appear where a detailed memo about the file can be written. For example, noting the interview was conducted in a noisy cafe shop. You can note that here.

![][image53]

4. Once you close the window, the memo will be automatically saved and linked to this file. You should see a small icon next to the interview in the list for the memo link when you have the interview list opened completely (with no other files open to the right of it). 

![][image54]

5. To view the memo link, right-click on the file again, select **Memo Link** and then **Open Linked Memo**.

![][image55]

6. To create an annotation for a snippet, go to **Interview** under **Files**, double-click on **Interview may13\_2015**.

![][image56]

7. In the detail view, select a text snippet, then select **New Annotation**.

![][image57]

8. A new box will appear at the bottom. Enter your annotation for this snippet. For example, “This part hasn't been cleaned yet.” Click anywhere outside of the box to save the annotation.

![][image58]

9. To see memos and annotations you have created all in one place, using the left navigation menu, under **Notes**.

![][image59]

10. Finally, you can also create a note that applies to the entire project, for example, maybe some ideas you have about how the research is going or new themes that are emerging. Right-click on **Memos** and select **New Memo**.

![][image60]

11. Give it a name, such as **Project Memo** and click **OK**.

![][image61]

12. Type some notes, such as “The project needs to be reviewed” and then close it to save. You can always double click on it from the list of memos to re-open it.

![][image62]

# **Image Coding** {#image-coding}

NVivo allows analyzing visual data by selecting and coding specific areas within an image. You can zoom in, highlight relevant parts of an image, and assign them to existing or new codes, making it possible to integrate visual analysis alongside textual and audio data within the same project.

1. Go to **Files** and click on **FG1 Questionnaire 14** to open the PDF file.

![][image63]

2. Note that NVivo 14 does not support **Optical Character Recognition (OCR)**. If your image files contain text that you want to code, make sure they are OCR-processed before importing them into NVivo. For text that cannot be OCRed (like handwriting or signatures), you can manually draw a square around the area you wish to code.

3. Under the **PDF** menu, select **Region**.

![][image64]

4. Draw a square around the area you want to code, then right-click and select **Code to Recent Codes**, then **Energy (Codes)**.

![][image65]

5. Now, go to **Codes** and double-click on **Energy**. In the detail view, instead of showing the image snippet, NVivo will display the coordinates of the selected image area. (On Mac, this will appear as a screenshot of the selected region.)

![][image66]

# **Save the Project** {#save-the-project}

1. During your work, the **Save Reminder** pop-up will appear periodically to remind you about the saving. Click **Yes** to confirm.

![][image67]

2. When you are done working on a project it is important to remember to save manually. First, go to the **File** menu.

![][image68]

3. Select **Save** to save the current project.

![][image69]

4. Alternatively, you can save a project by clicking on the floppy disk icon on the top right of the menu bar, or pressing **CTRL+S** on your keyboard.

![][image70]

5. Finally, you can close a project to return to the NVivo main screen. Once your project is saved, go back to the **File** menu and select **Close**.

![][image71]

# **Audio & Video Coding** {#audio-&-video-coding}

NVivo allows the import and analysis of audio and video files through coding specific time segments within those recordings. 

Please note that the **Transcription** feature in NVivo is not included in our software license; however, transcription can be done using alternative tools such as the **Dictate** feature in Microsoft Word.

1. From the main screen, click on **Sample Project (Multi-method)**. We will use this sample project for the rest of the workshop.

![][image72]

2. When the welcome pop-up appears, click **SKIP TOUR** to close it.

![][image73]

3. Go to **Files**, then **Interviews** folder. Double click to open the **Betty and Paul** file \- this is a video recording from an interview.

![][image74]

4. Opening this video recording gives us three panels: the audio waveform, the video playback window, and a content panel showing timestamps along with the transcript. Note that the layout may vary depending on the video \- some files may not include a transcript or have timestamps.

![][image75]

5. Now, go back to the **Interviews** folder, double-click on the **Helen** file \- this is an audio format file. 

![][image76]

6. Unlike the video format file, the audio recording gives us two panels: the audio waveform and a content panel showing timestamps along with the transcript. 

![][image77]

7. To code the segment, drag the **playhead** in the waveform window to the starting point, then click the **Start Selection** icon at the bottom to begin selecting the segment.

![][image78]

8. When it ends, click the **Finish Selection** icon to complete the coding range.

![][image79]

9. Then, right-click and select **Code Selection**. 

![][image80]

10. Select the code. For example, let’s select **Memorable quotes** in this case, and click **Code Selection to ‘Memorable qu…’** to confirm.

![][image81]

11. Go to **Codes**, **Memorable quotes**. The timestamp of the segment we just coded will appear.

![][image82]

12. To uncode a segment, click on the segment reference and go back to the source file.

![][image83]

13. From the audio wavement, locate to the coded segment, right-click it and select **Uncode** from the menu.

![][image84]

14. Select and check **Memorable quotes** from the pop-up, and click **OK**.

![][image85]

15. Now the coded segment should be removed.

16. Audio coding follows the same steps as video coding.

# **Case Classification & Cases** {#case-classification-&-cases}

Cases are a special type of code that represents the individuals in your study. If you have demographics or other important attributes that you want to incorporate into your study, case classifications and cases can help. For example, if you were analyzing interview transcripts, you might want to create a case classification called “Person” with attributes such as their name, age, education, job title, etc. Once your case classification is in place that defines what characteristics you want to capture for your interviewees, you could then create one case for each interviewee with those attributes filled in. 

For example, if you interviewed someone named Barbara, you would create a case called BARBARA (or some ID number if needed for confidentiality) with information about Barbara. You would then use that Barbara case to code all the imported content that are associated with Barbara (where the case acts like a code). Later you can then run queries that incorporate that information to answer questions such as, does Barbara talk more about the environment?

You can manually create case classifications and cases by using the left menu, under **Cases**. You can right click on **Case Classification** and **Create a New Classification** or right click on cases to create a new case. But often times, it is easier and more common to upload a spreadsheet with all the information for the cases. We are not going to try that out in this tutorial, but will show you how that would look like.

1. Under **Cases**, go to **Cases**, then **People.** Expand **Interview Participants** \- this will give us a list of interview participants.

![][image86]

2. Right-click on the name **Barbara**, select **Open Classification Sheet**.

![][image87]

3. A table of all the information about the participants will appear, with different attributes about their background, like the neighborhood they live in, their gender, age range, etc. You can edit the data here.

![][image88]

4. We can take advantage of NVivo’s autocoding features to identify the parts of interviewee and interviewers in a file and code them automatically into the appropriate case. Using the left menu, under **Data**, then **Files**, go to the **Interviews** folder and right-click on the interview transcript titled “Barbara”. Select **Autocode…**.

![][image89]

5. A wizard with different autocoding features will appear, which I encourage you to explore on your own. For now, let’s select the **Speaker name**. This is going to automatically code text based on the speaker name. Then click **Next**.

![][image90]

6. The “Barbara” document is formatted in a consistent manner so we can always pick out who is speaking because the person’s name is bolded followed by the words they speak. We need to specify who the unique speakers are in this document. Under **Enter all speakers**, type in **HENRY** and hit **Enter**. Then type in **BARBARA** and hit the **TAB** key. You should check the preview below to confirm that NVivo is picking up each unique speaker by highlighting them in different colours. If it looks correct, click on **Next**.

![][image91]

7. Make sure **Add to existing classification** is selected and from the drop-down next to it, **Person** is selected. Then click on **Finish**. This should code everything that Henry or Barbara said in the transcript with their cases.

![][image92]

8. Go to **Cases**, then go to **Cases**. 

![][image93]

9. Double click on the **BARBARA** case. You should see everything that Barbara said in her interview. These words are coded to this case. The BARBARA case code is now linked to Barbara’s interview responses.

![][image94]

10. Close all the tabs.

# **Query** {#query}

Instead of manually searching through large volumes of coded material, queries in NVivo are powerful tools that help you to quickly grab insight from the data by solving specific questions about your data such as how often certain words/phrases/themes appear, which participants expressed particular attitudes, or how concepts overlap.

This tutorial will not go through all of them in this workshop, but if you are interested in learning more, visit Windows version’s [Queries](https://help-nv.qsrinternational.com/14/win/Content/queries/queries.htm) page for additional resources. 

## **Word Frequency Query** {#word-frequency-query}

Word frequency query allows you to identify and analyze the most frequently used words across your sources.

1. First, let’s see what are the options we have. Go to the **Explore** menu to see all available query options. 

![][image95]

2. For Windows users, NVivo includes a feature called the **Query Wizard**, which assists in choosing the right query for your task and breaks down each option to help you understand how it works. Let’s try that first. Click on **Query Wizard**.

![][image96]

3. The pop-up gives 4 options corresponding to the four query types. Let’s select the second option \- **Word Frequency** query, which is described as “Identify frequently occurring terms in content.” You can also use Work Frequency query by clicking on **Work Frequency** under the **Explore** menu.

![][image97]

4. But now, let’s use **Query Wizard**. Select the second option, and click **Next**.

![][image98]

5. Set the “Display Words” field to 50, and keep the “Minimum Word Length” field set to 3\.

![][image99]

6. The **Grouping** option helps identify and organize similar or related terms in your text data to varying degrees. Same stem means words that share the same root or base form \- for example, talk, talking, talks, and talked all share the stem “talk.” Now, drag the bar to the second level, which groups words by the same stem, and click **Next**.

![][image100]

7. For the query scope, check **Selected Items**, then click on **Select…**

**![][image101]**

8. In the pop-up, expand **Files**, then click on **Interviews** to select everything in the folder. Next, unselect 2 videos and 1 audio files (with different icons) so that only text transcripts should be selected for our search. Click **OK**.

![][image102]

9. Click **Next**.

![][image103]

10. The last window asks you if you just want to run the query once or if you want to save it in your project so that you can later revisit. Let’s leave it as defaults for now and click **Run**.

![][image104]

11. Now we should see the results of our query.

![][image105]

12. Double-click on the word **people**, you will see the location of where the **people** appeared across all of the selected text transcripts.

![][image106]

13. Go back to the **Word Frequency Query Results**, and you will find out that words like ‘a’, ‘and’, ‘the’ are ignored \- these words are treated as **stop words**, which are those really common words and won’t be useful for analysis. When you see a word in the list and you don’t think they’d be helpful, for example, the word ‘things’, you can right-click on ‘things’ and select **Add to Stop Words List**.

![][image107]

14. To check or reset the Stop Words List, go to **File** menu, click on **Project Properties**.

![][image108]

15. Under the **General** tab, you can select text content languages. The default is English (US), but you can switch to other languages. Then, click on **Stop Words…** to see the current list in use. 

![][image109]

16. From here, you can add stop words manually, or reset the list. But for now, let’s click **Cancel**, then **Cancel** again to close the two pop-ups and return back to the result list.

![][image110]

17. Now let's export the list since we only selected **Run the query for once** in the past step. To do that, right-click on any word in the list, and select **Export List**. 

![][image111]

18. Browse to the workshop folder, give the file a name or keep the default and click on **Save**.

![][image112]

19. NVivo provides several visualization options for word frequency results. For example, click **Word Cloud** in the side tabs to view your results as a cloud.

![][image113]

20. Under the **Word Frequency Query** menu, you can choose to use another color palette and font style.

![][image114]

21. Right-click on the visual and select **Export Word Cloud** to save the word cloud in your computer.

![][image115]

22. Try out the **Tree Map** to see block-sized proportions by term.

![][image116]

23. Next, try out the **Cluster Analysis** to view relationships between terms.

![][image117]

24. Close the query to return to the main workspace for now.

![][image118]

## **Text Search Query** {#text-search-query}

Text Search Queries allow you to search for specific words or phrases across your project items.

1. Go to the **Explore** menu and select **Text Search Query**.

![][image119]

2. Keep the search scope as **Files & Externals** \- this includes all imported files in your project. In the search box, enter **water**, and drag the slider to **With stemmed words**.

![][image120]

3. Click **Run Query**.

![][image121]

4. A list of files containing the word **water** and its stemmed forms will appear. Double-click **Charles** to view the details.

![][image122]

5. In Charles’s interview transcript, you will see the term **water** highlighted.

![][image123]

6. We can store the results of this query as a new code. To do so, go back to the **Text Search Query – Results Preview** tab and click **Save Results…**. 

![][image124]

7. In the pop-up, click **Select** next to the **Location** field. 

![][image125]

8. Choose **Codes**, then click **OK**.

![][image126]

9. Rename the **Name** field to **Water**, and click **OK** again.

![][image127]

10. Go to **Codes** in the navigation view. You will see a new code named **Water**, showing the corresponding files and reference counts from the query.

![][image128]

11. If your search phrase contains multiple words, make sure to enclose it in quotation marks (“”). Otherwise, NVivo will treat each word as a separate search term. For example, enter “salt water” in the search box and click **Run Query** again.  
    * For more tips about building search query, visit [Text Search Query](https://help-nv.qsrinternational.com/14/win/Content/queries/text-search-query.htm) page.

![][image129]

12. Let’s say you want to save this query for future use. To do so, click **Save Criteria…**.

![][image130]

13. Name the query as **Salt Water**, and click **OK**.

![][image131]

14. Then, close the query tab.

![][image132]

15. Go to **Queries** in the navigation menu. Under **Query Criteria**, you can find **Salt Water** in the list. Double-click **Salt Water** to reopen the query we just saved.

![][image133]

## **Matrix Coding Query** {#matrix-coding-query}

Matrix Coding Query allows you to compare coding across multiple dimensions, such as codes, cases, or attributes, to identify patterns and relationships in your data. The results are displayed as a matrix table, where rows typically represent cases or participants and columns represent codes or themes. Each cell shows the number of references or the amount of coding coverage where the two dimensions intersect. 

For example, we can look at attitudes expressed by different interviewees based on what they said during the interviews. To run this query, we will use the code “Attitude” and the case “Interview Participants."

1. Go to the **Explore** menu and click **Matrix Coding Query**.

![][image134]

2. Under **Cases**, open **People**. In the list view, click the **\+** icon next to **Interview Participants** to expand the name list.

![][image135]

3. Select all participant names by dragging your cursor over them, then drag the selection into the **Rows** box.

![][image136]

4. Next, under **Codes**, expand **Attitude** by clicking the **\+** icon.

![][image137]

5. Select all items under the **Attitudes** code and drag them into the **Columns** box.

![][image138]

6. Make sure the search scope is set to **Files & Externals**, then click **Run Query**.

![][image139]

7. A matrix table will appear, showing the number of times participants mentioned words related to each attitude.

![][image140]

8. At the top-left of the page, click the **purple gradient palette** icon to apply color coding for easier visualization.

![][image141]

9. The table currently shows the total count of files where participants mentioned each attitude. To change the view, right-click anywhere on the table, select **Cell Content**, **Words Coded**.

![][image142]

10. This view displays the total count of coded words for each participant and attitude.

![][image143]

11. Try another view: right-click again, choose **Cell Content**, **Coding Presence**.

![][image144]

12. The table now shows **Yes** or **No**, indicating whether a participant mentioned that attitude or not.

![][image145]

13. To improve readability, right-click once more, select **Cell Shading**, **Green-Yellow-Red**.

![][image146]

14. The table now shows **Yes** in green and **No** in red.

![][image147]

15. You can select other visualization. Let’s click on the **Chart** tab to explore this visualization.

![][image148]

16. While 3D visualizations may look appealing, they can distort data interpretation and obscure important details. For clearer and more accurate results, consider exporting the query data and visualizing it using dedicated tools. See the [Data Visualization](https://library.dukekunshan.edu.cn/data-visualization/) guide for more information.

17. When finished, close the query tab to return to the main workspace.

![][image149]

# **Export Codes** {#export-codes}

When your analysis is complete, you can export your codes from NVivo in various formats \- as a code list, a codebook, or individual code files.

## **Code List** {#code-list}

1. Go to **Codes** under **Coding** and make sure the list of codes is open.

2. From the **Share** menu, select **Export**, **Export List**.

![][image150]

3. Keep the default file name (**Codes**), choose your workshop folder as the save location, and click **Save**.

![][image151]

4. Open the **Codes.xlsx** file in your workshop folder. You should see a list of all codes displayed in NVivo’s code list.

![][image152]

## **Codebook** {#codebook}

1. Go to **Codes** under **Coding** and make sure the list of codes is open.

2. From the **Share** menu, select **Export**, **Export Codebook**.

![][image153]

3. Keep the default file name (**Codebook – Environmental Change Down East**), check **Include number of files and references**, and click **OK**.

![][image154]

4. Open the **Codebook – Environmental Change Down East.doc** file in your workshop folder. This file displays each code with its description, and the counts of files and references associated with it.

![][image155]

## **Individual Code** {#individual-code}

1. Under **Codes**, select one or more codes to export.

2. Right-click on the selected area and choose **Export,** **Export Codes**.

![][image156]

3. In the **Export Options** pop-up, check **Summary View**, then click **OK**.

![][image157]

4. Each selected code will be saved as a separate file in your workshop folder. For example, opening the **Water** file will display the related reference files, their locations, reference counts, and coverage.

![][image158]

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
