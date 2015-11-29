# -*- coding: utf-8 -*-
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello World")
    
def people(request):
    html="""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"
    "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml"><!-- InstanceBegin template="/Templates/umn2-no breadcrumbs.dwt" codeOutsideHTMLIsLocked="false" -->
<head>
<style>
/* UNIVERSITY OF MINNESOTA WEB TEMPLATE RESET STYLESHEET */
/* AUGUST 2010 : UNIVERSITY RELATIONS */
/* v5  */

/* DO NOT MODIFY */
/* RESET */
html {background-color:#FFFFFF;color:#000000;}
body,div,h1,h2,h3,h4,h5,h6,pre,form,fieldset,input,textarea,p,th,td {margin:0;padding:0;}
table {border-collapse:collapse;border-spacing:0;}
fieldset,img {border:0;}
sup {vertical-align:text-top;}
sub {vertical-align:text-bottom;}

/* FONTS */
body {font:13px/1.231 arial,helvetica,clean,sans-serif;}
table {font-size:100%;}
th {font-style:normal;font-weight:normal;text-align:left;}
code {font-family:monospace;line-height:100%;}
input, textarea, select, option {font-family:arial,helvetica,clean,sans-serif;font-size:inherit;font-weight:inherit;}
h1,h2,h3,h4,h5,h6 {font-size:100%;font-weight:normal;}
em {font-style:italic;font-weight:normal;}
strong {font-style:normal;font-weight:bold;}
address,caption,cite,code,dfn,th,var {font-style:normal;font-weight:normal;}

/* FLOATS */
.left {float:left;}
.right {float:right;}
.clearabove {line-height:0;height:0;font-size:0;clear:both;} /* Use on a clearing element following a float */

/* HIDE */
.none {display:none;}
.hidden {visibility:hidden;overflow:hidden;width:0;height:0;}

/* Yahoo User Interface (YUI) FONT SIZING CHART: 10px=77% 11px=85% 12px=93% 13px=100% 14px=108% 15px=116% 16px=123.1% 17px=131% 18px=138.5% 19px=146.5% 20px=153.9% 21px=161.6% 22px=167% 23px=174% 24px=182% 25px=189% 26px=197% 
Find out more about YUI at http://developer.yahoo.com/yui/ */

body { color:#000000; font-family: Arial, Helvetica, sans-serif; line-height:18px; position: relative; }


/* LINKS */
a {color:#7a0019;}
a:link {color:#7a0019;}
a:hover {color:#362f2d;}
a:active {color:#362f2d;}
a:visited {color:#900021;}

/* HEADINGS *//* Basic Headline Set -- Adjust font sizes based on YUI chart above to maintain consistency. */
h1 { font-size:161%; line-height: 26px; color:#7a0019; margin-bottom: 10px; margin-top: 10px; }
h2 {font-size:138.5%;color:#7a0019;margin-bottom: 10px;line-height: 22px;margin-top: 12px;}
h3 { font-size:108%; color:#000000; margin-bottom: 10px; line-height: 22px; margin-top: 12px; font-style: italic; font-weight: bold; }
h4 {font-size:100%;color:#900021;text-transform:uppercase;}
h5 {font-size:93%;}
h6 {font-size:77%;}

/* TEXT *//* Basic Text Set */
p,ol, ul {font-size:97%;margin:0 0 .5em 0;}

/* List styles - edit as needed */
ul {list-style-type: disc; margin:0 5px 0px 5px;padding-bottom:10px;}
ol {list-style-type:decimal;margin:0 5px 0px 5px;padding-bottom:10px;}

@charset "UTF-8";
/* UNIVERSITY OF MINNESOTA WEB TEMPLATE STYLESHEET */
/* AUGUST 2010 : UNIVERSITY RELATIONS */
/* v4.090824 */


/* CENTER CONTAINER -- Centers the page in the browser */
body.center {margin-left:auto;margin-right:auto;width:960px;}

/*** HEADER, CAMPUS LINKS, UOFM HEADER, SEARCH BUTTONS, AND SEARCH BOX CSS ALL THANKS TO KIM DOBERSTEIN. THE STYLES DON'T USE THE GRID SYSTEM, BUT THE SEARCH BUTTON ALIGNMENT WORKS AND THE CSS NOW VALIDATES ***/

/************************** HEADER ***********************************/

#header{font-family:Arial, Helvetica, sans-serif;line-height:18px;color:#000;background:#fff;}
#header ul, #header li, #header p, #header div{font-size:11px;}


/******* Hide skip links *******************/
#skipLinks{ position:absolute; left:-9999px }

/*************************** CAMPUS LINKS ****************************/
#campus_links{text-align:right; background-color:#fff; padding-right:18px; line-height:22px;}

#campus_links a{color:#7a0019; /*Standard Maroon*/}
#campus_links a:hover{color:#666; /*Gray*/}

#campus_links ul, #campus_links li, #campus_links p{display:inline;}
#campus_links ul{margin:0;padding:0}
#campus_links li{margin-left:10px;}


/*************************** UOFM HEADER (MAROON BAR) ******************/

#headerUofM{position:relative;background:#7a0019 url(../../assets/img/bg_header.gif) repeat-x;height:63px;}

#logo_uofm{background:url(../../assets/img/logo_uofm_D2D.gif) no-repeat;height:62px;width:320px;}

#logo_uofm a,#logo_uofm a:hover{/*this should leave the link - but push the words into the hidden overflow */
display:block;height:62px; /*Must be same height as #logo_uofm*/width:0;padding-left:320px;/*Must be same as #logo_uofm width */overflow:hidden;}


/************************ SEARCH BUTTONS (MYU AND ONE STOP) *****************/
#search_area{position:absolute;right:0;top:0;text-align:right;}


#search_nav{position:absolute;right:10px;text-align:right;top:5px;}

#search_nav a{display:block;float:right;width:0px;height:25px;padding-left:73px;overflow:hidden;margin-left:5px;}

#btn_myu{background:url(../../assets/img/btn_myu.gif);}

#btn_onestop{background:url(../../assets/img/btn_onestop.gif);}


/******************* SEARCH BOX ************************************/

#gsearch{background: url(../../assets/img/search_field.gif) no-repeat; /* #f3c */height:22px ;width:269px;position:relative;top:35px;}

#gsearch label{position:absolute; left:-9999px}

#search_field{border:0;color:#666666;width:200px;position:absolute;top:3px;left:15px;font-size:11px;color:#333;}


/* For the print style sheet */
.leftprint, .rightprint { display:none;}


/* 960 GRID
--------------------------------------------------------------------------------*/
/* Change the background image to create various column separations on the page*/

.container_12 { height: 100%; clear: both; border-bottom: 3px solid #e4e4e4; margin-left: auto; margin-right: auto; float: left; width: 100%; }

#bg264 { background-color: #FFFFFF; background-repeat: repeat-y; float: left; background-image: url(../../assets/img/bg_2.6.4.gif); }
#bg273 { background-color: #FFFFFF; background-image: url(../../assets/img/bg_2.7.3.gif); background-repeat: repeat-y; float: left; }
#bg354 { background-color: #FFFFFF; background-image: url(../../assets/img/bg_3.5.4.gif); background-repeat: repeat-y; float: left; }
#bg210 { background-color: #FFFFFF; background-image: url(../../assets/img/bg_2.10.0.gif); background-repeat: repeat-y; float: left; } /* Added by Gary for VHLab */
#bg39 { background-color: #FFFFFF; background-image: url(../../assets/img/bg_3.9.gif); background-repeat: repeat-y; float: left; } /* Added by Gary for VHLab */


.grid_1,.grid_2,.grid_3,.grid_4,.grid_5,.grid_6,.grid_7,.grid_8,.grid_9,.grid_10,.grid_11,.grid_12 {display: inline;float: left;}

.container_12 .grid_1 {width: 80px;}
.container_12 .grid_2 {width: 160px;}
.container_12 .grid_3 {width: 240px;}
.container_12 .grid_4 {width: 320px;}
.container_12 .grid_5 {width: 400px;}
.container_12 .grid_6 {width: 480px;}
.container_12 .grid_7 {width: 560px;}
.container_12 .grid_8 {width: 640px;}
.container_12 .grid_9 {width: 720px;}
.container_12 .grid_10 {width: 800px;}
.container_12 .grid_11 {width: 880px;}
.container_12 .grid_12 {width: 960px;}


.alpha {margin-left: 0;}
.omega {margin-right: 0;}
	
/* Removes the space around the header graphic */
#nospace {margin: 0;}
.nopadding { padding: 0; }


/* BODY CONTENT
--------------------------------------------------------------------------------*/

/* Adds padding to text in columns so that text doesn't span the full width of the grid column*/
p,h1,h2,h3 {padding-left:10px; padding-right:10px;} 
p {padding-bottom: 6px}
p.single_space {padding-bottom: 0px; padding-top: 0px; line-height:100%; margin-bottom:0px;}
table.vhlab_padded {margin-left: 10px; margin-right:10px;} /* Added by Gary for VHLab - fix padding around tables */
table.vhlab_padded_inside {margin-left: 10px; margin-right:10px;} /* Added by Gary for VHLab - fix padding around tables */
table.vhlab_padded_inside td {padding:5px;} /* Added by Gary for VHLab - fix padding within tables */


/* Styles headings on the home page to be the same size as those on secondary pages. */
h2.home {font-size:161%;}
h3.home { font-size:138.5%; color:#7a0019; font-style: normal; font-weight: normal; }


/* Styles for left navigation */
/* #main_nav_2 {line-height: 25px; width: 160px;margin: 0;} */ /* Original before edited by Gary for VHLab */
#main_nav_2 {line-height: normal; width: 160px;margin: 0;}
#main_nav_3 { margin: 10px 20px 0 0; line-height: 25px; width: 220px; }
/* ul.main_nav li {margin:2px 0 0 -30px;list-style:none;} */ /* Original before edited by Gary for VHLab */
ul.main_nav li {margin:2px 0 0 -30px;list-style:none; padding-bottom:10px;}
ul.main_nav li a {color:#7a0019; text-decoration:none;}
ul.main_nav li a:link {text-decoration:none; color:#7a0019;}
ul.main_nav li a:hover { color:#362f2d; border-bottom: 1px solid #998675;}
ul.main_nav li a:active {color:#362f2d;}
ul.main_nav li a:visited {color:#900021;}

.vhlab_headline { font-size: 138.5%; color:#7a0019;} /* Added by Gary for VHLab - effective h2 without being a heading */
.vhlab_maroon { color:#7a0019;} /* Added by Gary for VHLab - change font color to maroon */

.relatedlinks { font-size: 116%; font-weight: bold; margin-left: 0; margin-right:1px; padding-top:16px;}

/* BREADCRUMBS */
/* Use with template 2.6.4 */
.breadcrumbs { padding-top: 2px; padding-bottom: 4px; border-bottom-width: 1px; border-bottom-style: solid; border-bottom-color: #bbb7b0; }
/* Use with template 2.7.3 */
.crumb { padding-top: 4px; border: none 0; border-bottom: 3px solid #e4e4e4;border-right: 3px solid #e4e4e4; border-left: 3px solid #e4e4e4; background: #FFFFFF; }


/* Removes link lines and other unsightly blemishes */
.noline {text-decoration: none;}

/*FOOTER*/

#footer_inner { padding:5px 0 0 0; font-size: 90%; width:500px; background: #FFFFFF; }
.copyright { float:left; margin-left: -30px; list-style:none;}

#footer_right{ font-size: 90%; padding:5px 0 0 0; float: right; width: 460px; text-align: right; background: #FFFFFF; }
ul.footer_links {float:right;padding-right: 10px; list-style:none;}
ul.footer_links li { display:inline; padding-left: 10px; }
ul.footer_links li a {color:#7a0019; text-decoration:none; border-bottom:1px solid #c2a9ae;}
ul.footer_links li a:link {color:#7a0019;}
ul.footer_links li a:visited {color:#900021;}
ul.footer_links li a:hover { color:#666666; border-bottom: 1px solid #666666; }
ul.footer_links li a:active {color:#666666;}


/* =CLEAR FLOATED ELEMENTS
--------------------------------------------------------------------------------*/

/* http://sonspring.com/journal/clearing-floats */

html body * span.clear,
html body * div.clear,
html body * li.clear,
html body * dd.clear
{background: none;border: 0;clear: both;display: block;float: none;font-size: 0;list-style: none;margin: 0;padding: 0;overflow: hidden;visibility: hidden;width: 0;height: 0;}

/* http://www.positioniseverything.net/easyclearing.html: See print out of this article. This fix should not be needed with overflow:auto added to the outer div */

.clearfix:after {clear: both;content: '.';display: block;visibility: hidden;height: 0;}
.clearfix {display: inline-block;}
* html .clearfix {height: 1%;}

.clearfix {display: block;}

@charset "UTF-8";
/* UNIVERSITY OF MINNESOTA OPTIONAL WEB TEMPLATE STYLESHEET */
/* FEBRUARY 2010 : UNIVERSITY RELATIONS*/
/* v3.090219  */

/*OPTIONAL HORIZONTAL NAVIGATION*/
#header_sub {behavior:url("../lib/htc/csshover2.htc");} /*Fix for IE's lack of support for :hover*/
#header_sub {height:100%;line-height:30px;font-size:90%;color:#FFFFFF;text-align:right;background:#7A0019 url(../../assets/img/bg_header_sub.gif) top left repeat-x;border-top:1px solid #5b0013;border-bottom: 1px solid #5b0013;}
#header_sub ul#header_sub_nav {margin:0 12px 0 0;display:inline;float:right; list-style:none;}
#header_sub ul#header_sub_nav li.tl_menu {display:inline;float:left;position:relative;}
#header_sub ul#header_sub_nav li.tl_menu a {display:block;color:#FFFFFF;font-weight:bold;padding:0 5px;text-decoration: none;}
#header_sub ul#header_sub_nav li.tl_menu a:hover {color:#FFB71E;}


/* DROP DOWN MENU FOR OPTIONAL HORIZONTAL NAVIGATION*/
div.dd_menu_top { background:transparent url(../../assets/img/dd_menu_bottom.gif) bottom left no-repeat; width:144px;}
ul.dd_menu {background:transparent url(../../assets/img/dd_menu_top.gif) top left no-repeat;text-align:center;line-height:15px;padding:10px 1px 0;margin-bottom:10px;margin-left:0px; margin-right:0; list-style:none;}
.dd_last ul.dd_menu {background-image:url(../../assets/img/dd_menu_top_end.gif);}
#header_sub ul#header_sub_nav li.tl_menu ul.dd_menu li {border-bottom:1px solid #fdd67b;}
#header_sub ul#header_sub_nav li.tl_menu ul.dd_menu li a {width:142px;margin:0;padding:2px 0;color:#333333;font-weight:normal;}
#header_sub ul#header_sub_nav li.tl_menu ul.dd_menu li a:hover {background-color:#E3E3E3;color:#333333;}
#header_sub ul#header_sub_nav li.tl_menu div.dd_menu_top {position:absolute;left:-999em;top:25px;z-index:999;}
#header_sub ul#header_sub_nav li.tl_menu:hover div.dd_menu_top {visibility:visible;}
#header_sub ul#header_sub_nav li.tl_menu:hover div#nav_cat1 {left:-45px;}
#header_sub ul#header_sub_nav li.tl_menu:hover div#nav_cat2 {left:-18px;}
#header_sub ul#header_sub_nav li.tl_menu:hover div#nav_cat3 {left:-23px;}
#header_sub ul#header_sub_nav li.tl_menu:hover div#nav_cat4 {left:-30px;}
#header_sub ul#header_sub_nav li.tl_menu:hover div#nav_cat5 {left:-55px;}



/*UNIT NAME FOR OPTIONAL HORIZONTAL NAVIGATION*/
.unit { display:inline; float:left; color:#FFDE7A; margin-left:10px; font-size:90%; }
.unit a {color:#FFDE7A;text-decoration:none;}
.unit a:hover {color:#FFFFFF;text-decoration:none;}
.unit a:visited {color:#FFDE7A;text-decoration:none;}


/*OPTIONAL UNIT FOOTER*/
#unit_footer {font-size:90%;;border-bottom: 3px solid #e4e4e4;padding: 5px 0 0 0;line-height: 20px;width: 960px;}
#unit_footer1 {font-size:90%;;border-bottom: 3px solid #e4e4e4;padding:5px 0 0 0;background-color: #e4e4e4;line-height: 20px;width: 960px;}
#unit_footer2 {font-size:90%;;border-bottom: 3px solid #e4e4e4;padding:5px 0 0 0;background-color: #d4cfc7;line-height: 20px;width: 960px;}

/* set the float to left for left-aligned links, or right for right-aligned links*/
ul.unit_footer_links { float:right; padding-left: 10px; padding-right: 10px; }
ul.unit_footer_links li { display:inline; padding: 5px; }
ul.unit_footer_links li a {color:#7a0019;text-decoration: none;border-bottom: 1px solid #c2a9ae;}
ul.unit_footer_links li a:link {color:#7a0019;}
ul.unit_footer_links li a:visited {color:#900021;}
ul.unit_footer_links li a:hover {color:#666666;}
ul.unit_footer_links li a:active {color:#666666;}

.acronym_border { border-bottom-style: none; }
</style>
<!-- University of Minnesota Web template:  v5.101021 -->

<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<meta name="Description" content="University of Minnesota" />
<meta name="Keywords" content=" " />

<!-- InstanceBeginEditable name="doctitle" -->
<title>The Visible Heart&reg; Laboratory</title>
<!-- InstanceEndEditable -->
<link rel="shortcut icon" href="http://www1.umn.edu/twincities/favicon.ico" type="image/x-icon" />


<link href="/lib/css/reset.css" rel="stylesheet" type="text/css" media="screen" />
<link href="/lib/css/template.css" rel="stylesheet" type="text/css" media="screen" />
<link href="/lib/css/optional.css" rel="stylesheet" type="text/css" media="screen" />
<link href="/lib/css/print.css" rel="stylesheet" type="text/css" media="print" />
<script type="text/javascript" src="lib/js/searchfield.js"></script>

<!-- Add your unit's style sheet(s) here -->
<!-- BEGIN Rollover script items -->
<script type="text/javascript">
<!--
function MM_swapImgRestore() { //v3.0
  var i,x,a=document.MM_sr; for(i=0;a&&i<a.length&&(x=a[i])&&x.oSrc;i++) x.src=x.oSrc;
}
function MM_preloadImages() { //v3.0
  var d=document; if(d.images){ if(!d.MM_p) d.MM_p=new Array();
    var i,j=d.MM_p.length,a=MM_preloadImages.arguments; for(i=0; i<a.length; i++)
    if (a[i].indexOf("#")!=0){ d.MM_p[j]=new Image; d.MM_p[j++].src=a[i];}}
}

function MM_findObj(n, d) { //v4.01
  var p,i,x;  if(!d) d=document; if((p=n.indexOf("?"))>0&&parent.frames.length) {
    d=parent.frames[n.substring(p+1)].document; n=n.substring(0,p);}
  if(!(x=d[n])&&d.all) x=d.all[n]; for (i=0;!x&&i<d.forms.length;i++) x=d.forms[i][n];
  for(i=0;!x&&d.layers&&i<d.layers.length;i++) x=MM_findObj(n,d.layers[i].document);
  if(!x && d.getElementById) x=d.getElementById(n); return x;
}

function MM_swapImage() { //v3.0
  var i,j=0,x,a=MM_swapImage.arguments; document.MM_sr=new Array; for(i=0;i<(a.length-2);i+=3)
   if ((x=MM_findObj(a[i]))!=null){document.MM_sr[j++]=x; if(!x.oSrc) x.oSrc=x.src; x.src=a[i+2];}
}
//-->
</script>
<!-- END Rollover script items -->

<!-- STYLE SHEETS TO FIX INTERNET EXPLORER INCONSISTENCIES -->

<!--[if IE 6]>
<style type="text/css" media="screen">
@import url("lib/css/IE6.css");
</style>
<![endif]-->
<!--[if IE 7]>
<style type="text/css" media="screen">
@import url("lib/css/IE7.css");
</style>
<![endif]-->

</head>


<body class="center">

<!--BEGIN WORDMARK AND UNIT IDENTIFICATION FOR PRINT -->
<!--Use this code along with the print.css to retain the University's wordmark on your printed Web pages and to identify your unit -->
<div class="leftprint">
<img src="/assets/img/smMwdmk.gif" alt="University of Minnesota" width="216" height="55" hspace="10" align="left" />
</div>
<div class="rightprint"><strong>University of Minnesota</strong><br />
http://www.umn.edu/<br />
612-625-5000<br />
</div>
<!--END WORDMARK AND UNIT IDENTIFICATION FOR PRINT -->



<!--  Skip Links  -->
  <p id="skipLinks">
  	<a href="#main_nav">Main navigation</a> | 
    <a href="#maincontent">Main content</a>
  </p>

<div id="header">

 <!-- BEGIN CAMPUS LINKS -->
    <div id="campus_links">
        <p>Campuses: </p>
        <ul>
          <li><a href="http://www.umn.edu">Twin Cities</a></li>
          <li><a href="http://www.crk.umn.edu">Crookston</a></li>
          <li><a href="http://www.d.umn.edu">Duluth</a></li>
          <li><a href="http://www.morris.umn.edu">Morris</a></li>
          <li><a href="http://www.r.umn.edu">Rochester</a></li>
          <li><a href="http://www.umn.edu/campuses.php">Other Locations</a></li>
        </ul>
    </div>
    <!-- END CAMPUS LINKS -->
      
      
    <!--  BEGIN TEMPLATE HEADER (MAROON BAR) -->
    <div id="headerUofM">
        
    <div id="logo_uofm"><a href="http://www.umn.edu/">Go to the U of M home page</a></div>
        

 <!--BEGIN search div-->
      <div id="search_area">
       <div id="search_nav"><a href="http://onestop.umn.edu/" id="btn_onestop">OneStop</a> <a href="https://www.myu.umn.edu/" id="btn_myu">myU</a></div>
         
<div class="search"> 
<form action="http://google.umn.edu/search" method="get" name="gsearch" id="gsearch" title="Search U of M Web sites">
<label for="search_field">Search U of M Web sites</label>
<input type="text" id="search_field" name="q" value="Search U of M Web sites"  title="Search text"  />   
<input class="search_btn" type="image" src="/assets/img/search_button.gif" alt="Submit Search" value="Search" />
<input name="client" value="searchumn" type="hidden" />
<input name="proxystylesheet" value="searchumn" type="hidden" />
<input name="output" value="xml_no_dtd" type="hidden" />
</form>  
</div> 
         
</div></div>
<!-- end search area -->
     
</div>
<!-- End search div -->

<!--END UofM TEMPLATE HEADER-->

<!-- BEGIN PAGE CONTENT -->

<!-- BEGIN TWO COLUMN PAGE CONTENT -->
<div class="container_12" id="bg210">

<!--BEGIN LEFT NAVIGATION -->

 
<div class="grid_2" id="main_nav_2">
<a href="http://www.surg.umn.edu/" target="_blank" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('DoS','','/graphics/DepartmentofSurgery-over.gif',1)"><img src="/graphics/DepartmentofSurgery.gif" alt="Department of Surgery" name="DoS" width="160" height="58" border="0" /></a><br />
<a href="http://www.med.umn.edu/" target="_blank" onmouseout="MM_swapImgRestore()" onmouseover="MM_swapImage('MedSchool','','/graphics/MedSchool-over.gif',1)"><img src="/graphics/MedSchool.gif" alt="Medical School" name="MedSchool" width="160" height="59" border="0" /></a><br />
<a name="mainnav" id="main_nav"></a>
<ul class="main_nav">
<li class="relatedlinks"><b>Principal Investigator</b></li>
<li><a href="/pai/index.html">Paul A. Iaizzo, PhD, FHRS</a></li>
<li><img src="staff/pics/Paul_Iaizzo2.jpg" alt="" name="paul" width="85" height="100" id="paul" /></li>
<li class="relatedlinks"><b>Public links</b></li>
<li><a href="/about.html">About the lab</a></li>
<li><a href="/people.html">People</a></li>
<li><a href="/upcoming_events.html">Upcoming Events </a></li>
<li><a href="/media.html">VH Lab in the media</a></li>
<li><a href="/news-events.html">Lab News</a></li>
<li><a href="/research/index.html">Research</a></li>
<li><a href="/publications.html">Publications</a></li>
<li><a href="/malignant-hyperthermia.html">Malignant Hyperthermia</a></li>
<li><a href="/affiliations.html">Affiliations</a></li>
<li><a href="/courses.html">Courses/Educational Outreach </a></li>
<li><a href="/atlas/index.shtml">Atlas of Human Cardiac Anatomy</a></li>
<li><a href="/bears/">Minnesota Black Bear Research</a></li>
<li><a href="/gift.html"><img src="/graphics/VHLab-gift.gif" alt="Make a Gift" height="66" width="140" border="0" /></a></li> 
<li class="relatedlinks"><b>Secure links</b></li>
<li><a href="/secure/index.html">Lab login</a></li>
</ul>

</div>

<!-- END LEFT NAVIGATION -->

<!-- BEGIN Unit Graphic Header for home page -->
<div id="main_head" class="grid_10">
  <p id="nospace" class="nopadding"><a href="/index.html"><img src="/graphics/VHLlogo2013Black.gif" alt="Go to unit's home." width="800" height="117" /></a></p>
</div>
<!-- END Unit Graphic Header for home page -->

<!-- BEGIN CENTER COLUMN -->
<div class="grid_10">
<a name="maincontent" id="maincontent"></a>
<!-- InstanceBeginEditable name="Main information section" -->
      <h1>Principal Investigator</h1>
      <table border="1" cellpadding="2" cellspacing="0" class="vhlab_padded">
        <tr>
          <td width="100" valign="top"><div align="center"><img src="staff/pics/Paul_Iaizzo2.jpg" alt="paul_pi" width="85" height="100" /></div></td>
          <td width="200" valign="top"><p><strong>Paul Iaizzo, PhD, FHRS </strong> <br />
          Professor </p></td>
          <td width="220" valign="top"><p><a href="mailto:iaizz001@umn.edu">iaizz001@umn.edu</a><br />
                  <a href="/pai/index.html">website</a><br />
          612-624-7912 </p></td>
        </tr>
    </table>
      <p>&nbsp; </p>
      <h1>Laboratory Staff</h1>
      <table border="1" cellpadding="2" cellspacing="0" class="vhlab_padded">
            <tr>
              <td valign="top"><div align="center"><img src="staff/pics/Tinen_staff_pic_2013.jpg" width="100" height="104" /></div></td>
              <td width="200" valign="top"><p><strong>Tinen Iles</strong><br />Assistant Scientist </p></td>
              <td width="220" valign="top"><p><a href="mailto:thealy@umn.edu">thealy@umn.edu</a><br />
                612-625-3641</p></td>
            </tr>
            <tr>
              <td width="100" valign="top"><div align="center"><img src="staff/pics/Monica_staff_pic_2013.jpg" width="100" height="105" /></div></td>
              <td width="200" valign="top"><p align="left"><strong>Monica Mahre</strong><br />
              Lab Services Coordinator</p></td>
              <td width="220" valign="top"><p><a href="mailto:mahre002@umn.edu">mahre002@umn.edu</a><br />
                612-624-3959</p></td>
            </tr>
            <tr>
              <td width="100" valign="top"><div align="center"><img src="staff/pics/Charles_staff_2013.jpg" width="100" height="103" /></div></td>
              <td width="200" valign="top"><p align="left"><strong>Charles Soule</strong><br />
              Scientist</p></td>
                <td width="220" valign="top"> 
                  <p><a href="mailto:soule005@umn.edu">soule005@umn.edu</a><br />
                  612-626-2518</p></td>
            </tr>
            <tr>
              <td width="100" valign="top"><div align="center"><img src="staff/pics/Gary_web_pic_2013.jpg" width="100" height="106" /></div></td>
              <td width="200" valign="top"><p align="left"><strong>Gary Williams</strong><br />
              Applications Programmer</p></td>
              <td width="220" valign="top"><p><a href="mailto:willi067@umn.edu">willi067@umn.edu</a><br />
                612-624-3161</p>              </td>
            </tr>
      </table>
      <p>&nbsp;</p>
      <h1>Adjunct Assistant Professors </h1>
      <table border="1" cellpadding="2" cellspacing="0" class="vhlab_padded">
        <tr>
          <td width="100" height="102" valign="top"><div align="center"><img src="staff/pics/Michael_Eggen_Photo4.jpg" alt="Mike Eggen" width="100" height="120" /></div></td>
          <td width="200" valign="top"><p><strong>Michael Eggen, PhD </strong><strong></strong><br />
            Principal Scientist Medtronic </p>
            <p align="left"><br />
          </p></td>
          <td width="220" valign="top"><p><a href="michael.d.eggen@medtronic.com">michael.d.eggen@medtronic.com</a><br />
            763-526-0192</p></td>
        </tr>
        <tr>
          <td width="100" height="102" valign="top"><div align="center"><img src="staff/pics/AlexHill.jpg" width="100" height="100" /></div></td>
          <td width="200" valign="top"><p><strong>Alexander Hill </strong>,<strong> PhD </strong><br /> 
            Research Manager- Medtronic</p></td>
          <td width="220" valign="top"><p><a href="mailto:mahre002@umn.edu">alex.hill@medtronic.com</a><br />
          763-514-9776</p></td>
        </tr>
        <tr>
          <td width="100" valign="top"><div align="center"><img src="staff/pics/TimLaske_2.jpg" width="100" height="98" /></div></td>
          <td width="200" valign="top"><p align="left"><strong>Timothy Laske</strong>,<strong> PhD </strong><br />
          Vice President of Product Development - Medtronic AF Solutions</p></td>
          <td width="220" valign="top"><p><a href="mailto:soule005@umn.edu">tim.g.laske@medtronic.com</a><br />
          763-514-9782</p></td>
        </tr>
        <tr>
          <td width="100" valign="top"><div align="center"><img src="staff/pics/Nick_Skadsberg.jpg" width="100" height="100" /></div></td>
          <td width="200" valign="top"><p align="left"><strong>Nicholas Skadsberg</strong>,<strong> PhD </strong><br />
          Senior Marketing Manager- Medtronic AF Solutions</p>          </td>
          <td width="220" valign="top"><p><a href="mailto:willi067@umn.edu">nick.skadsberg@medtronic.com</a><br />
          763-526-0163</p></td>
        </tr>
      </table>
	  
      <p>&nbsp;</p>
      <h1><a name="top" id="top"></a>Students</h1>
            <p> 
              <!-- <a href="#postdoc">Research and Post-Doctoral Fellows</a>,  -->
              <a href="#doctoral">Doctoral</a>, 
              <a href="#masters">Masters</a>, <a href="#medical">Medical</a>, <a href="#volunteers">Volunteers/Directed Research</a>, <a href="former_students.html">Former students</a></p>
<!--
            <h2><a name="post-doctoral" id="post-doctoral"></a>Post-Doctoral</h2>
            <p><a href="#top">return to top</a></p>
            <p>&nbsp;</p>
-->
            <h2><a name="doctoral" id="doctoral"></a>Doctoral/Postdoctoral Students</h2>
            <table border="1" cellpadding="2" cellspacing="0" class="vhlab_padded">
              <tr>
                <td valign="top"><img src="students/pics/ErikGaasedelen.jpg" width="100" height="100" /></td>
                <td width="200" valign="top"><p><strong>Erik Gaasedelen</strong><br />
                  Bioinformatics and Computational Biology</p>
                  <p>&nbsp; </p></td>
                <td width="220" valign="top"><p><a href="mailto:gaas0012@umn.edu">gaas0012@umn.edu</a></p>
                <p>&nbsp;</p></td>
              </tr>
              <tr>
                <td width="100" valign="top"><img src="students/pics/BrianHoward.jpg" width="100" height="100" /></td>
                <td width="200" valign="top"><p><strong>Brian Howard</strong><br />
                Biomedical Engineering </p></td>
                <td width="220" valign="top"><p><a href="mailto:howa0236@umn.edu">howa0236@umn.edu</a></p></td>
              </tr>
              <tr>
                <td valign="top"><img src="/staff/pics/Tinen_staff_pic_2013.jpg" width="100" height="104" /></td>
                <td width="200" valign="top"><p><strong>Tinen Iles</strong><br />
                Bioinformatics and Computational Biology</p>                </td>
                <td width="220" valign="top"><p><a href="mailto:thealy@umn.edu">thealy@umn.edu</a></p>
                <p>&nbsp;</p></td>
              </tr>
              <tr>
                <td valign="top"><img src="students/pics/LarsMattison.jpg" width="100" height="100" /></td>
                <td width="200" valign="top"><p><strong>Lars Mattison </strong><br />
                Biomedical Engineering</p>                </td>
                <td width="220" valign="top"><p><a href="mailto:matti137@umn.edu">matti137@umn.edu</a></p>                </td>
              </tr>
              <tr>
                <td valign="top"><img src="students/pics/AlexMattson.jpg" width="100" height="100" /></td>
                <td width="200" valign="top"><p><strong>Alex Mattson</strong><br />
                Biomedical Engineering </p>                </td>
                <td width="220" valign="top"><p><a href="mailto:matts460@umn.edu">matts460@umn.edu</a></p>
                <p>&nbsp;</p></td>
              </tr>
              <tr>
                <td valign="top"><img src="students/pics/MeganSchmidt.jpg" width="100" height="100" /></td>
                <td width="200" valign="top"><p><strong>Megan Schmidt </strong><br />
                Biomedical Engineering</p>                </td>
                <td width="220" valign="top"><p><a href="mailto:schm2696@umn.edu">schm2696@umn.edu</a></p>                </td>
              </tr>
              <tr>
                <td valign="top"><img src="students/pics/JohnSpratt.jpg" width="100" height="100" /></td>
                <td width="200" valign="top"><p><strong>John Spratt</strong><br />
                Resident, General Surgery </p>                </td>
                <td width="220" valign="top"><p><a href="mailto:sprat020@umn.edu">sprat020@umn.edu</a></p>                </td>
              </tr>
            </table>
          <a href="#top">return to top</a><br />
          <p>&nbsp;</p>
            <h2><a name="masters" id="masters"></a>Masters Students </h2>
            <table border="1" cellpadding="2" cellspacing="0" class="vhlab_padded">
              <tr>
                <td valign="top"><div align="center"><img src="students/pics/MariaBurbano.jpg" width="81" height="100" /></div></td>
                <td valign="top"><p><strong>Maria Burbano</strong></p>                </td>
                <td valign="top"><p><a href="mailto:burba040@umn.edu">burba040@umn.edu</a><br />
                  214-705-5831</p>                </td>
              </tr>
              <tr>
                <td valign="top"><div align="center"><img src="students/pics/SalahElHaddi.jpg" alt=" " width="100" height="100" /></div></td>
                <td width="200" valign="top"><p><strong>Salah James El Haddi</strong><br />
                  Medical Student<br />
                  (MD/MS Program) </p></td>
                <td width="220" valign="top"><p><a href="mailto:elha0027@umn.edu">elha0027@umn.edu</a></p>
                    <p>&nbsp;</p></td>
              </tr>
              <tr>
                <td valign="top"><div align="center"><img src="students/pics/MeganHarris.jpg" width="100" height="100" /></div></td>
                <td width="200" valign="top"><p><strong>Megan Harris</strong><br />
                  Biomedical Engineering</p>                  </td>
                <td width="220" valign="top"><p><a href="mailto:harr1470@umn.edu">harr1470@umn.edu</a></p>                </td>
              </tr>
              <tr>
                <td valign="top"><div align="center">Picture not <br />
                available</div></td>
                <td width="200" valign="top"><p><strong>Ross Hinrichsen</strong><br />
                </p>                </td>
                <td width="220" valign="top"><p><a href="mailto:hinri153@umn.edu">hinri153@umn.edu</a></p>                </td>
              </tr>
              <tr>
                <td valign="top"><div align="center"><img src="students/pics/AlyssaJackson.jpg" width="100" height="100" /></div></td>
                <td width="200" valign="top"><p><strong>Alyssa Jackson</strong><br />
                  Biomedical Engineering </p>                  </td>
                <td width="220" valign="top"><p><a href="mailto:jacks938@umn.edu">jacks938@umn.edu</a></p>                </td>
              </tr>
              <tr>
                <td valign="top"><div align="center"><img src="students/pics/EvanJohnson.jpg" width="100" height="100" /></div></td>
                <td width="200" valign="top"><p><strong>Evan Johnson</strong><br />
                  Biomedical Engineering
</p>                </td>
                <td width="220" valign="top"><p><a href="mailto:joh10385@umn.edu">joh10385@umn.edu</a></p>                </td>
              </tr>
              <tr>
                <td valign="top"><div align="center"><img src="students/pics/LanceRongstad.jpg" width="100" height="100" /></div></td>
                <td width="200" valign="top"><p><strong>Lance Rongstad</strong><br />
                  Biomedical Engineering</p>                </td>
                <td width="220" valign="top"><p><a href="mailto:rongs005@umn.edu">rongs005@umn.edu</a></p>                </td>
              </tr>
              <tr>
                <td valign="top"><div align="center">Picture not <br />
                available</div></td>
                <td width="200" valign="top"><p><strong>Tony Schmitz</strong><br />
                  Biomedical Engineering</p>                  </td>
                <td width="220" valign="top"><p><a href="mailto:schm2910@umn.edu">schm2910@umn.edu</a></p>                </td>
              </tr>
              <tr> 
                <td width="100" valign="top"><div align="center"><img src="students/pics/ScottSkorupa.jpg" width="100" height="100" /></div></td>
                <td width="200" valign="top"><p><strong>Scott Skorupa</strong><br />
                  Biomedical Engineering</p></td>
                <td width="220" valign="top"><p><a href="mailto:saskorupa@gmail.com">saskorupa@gmail.com</a></p></td>
              </tr>
              <tr>
                <td valign="top"><div align="center"><img src="students/pics/JeremyStimack.jpg" width="100" height="100" /></div></td>
                <td valign="top"><p><strong>Jeremy Stimack</strong><br />
                  Biomedical Engineering</p>                </td>
                <td valign="top"><p><a href="mailto:stim0046@umn.edu">stim0046@umn.edu</a></p>                </td>
              </tr>
              <tr> 
                <td width="100" valign="top"><div align="center"><img src="students/pics/MattYoder.jpg" width="100" height="100" /></div></td>
                <td width="200" valign="top"><p><strong>Matt Yoder</strong><br />
                  Biomedical Engineering</p></td>
                <td width="220" valign="top"><p><a href="mailto:yoder027@umn.edu">yoder027@umn.edu</a></p></td>
              </tr>
            </table>
          <a href="#top">return to top</a><br />
          <p>&nbsp;</p>
            <h2><a name="medical" id="medical"></a>Medical/Veterinary Medicine Students </h2>
            <table border="1" cellpadding="2" cellspacing="0" class="vhlab_padded">
              <tr>
                <td width="96" valign="top"><div align="center"><img src="students/pics/ChenChen.jpg" width="100" height="100" /></div></td>
                <td width="194" valign="top"><p><strong>Chen Chen</strong><br />
                Medical Student </p>                </td>
                <td width="219" valign="top"><p><a href="mailto:chenx555@umn.edu">chenx555@umn.edu</a></p>                </td>
              </tr>
              <tr>
                <td width="96" valign="top"><div align="center"><img src="students/pics/SalahElHaddi.jpg" width="100" height="100" /></div></td>
                <td width="194" valign="top"><p><strong>Salah James El Haddi</strong><br />
                  Medical Student<br />
                  (MD/MS Program)
</p>                </td>
                <td width="219" valign="top"><p><a href="mailto:elha0027@umn.edu">elha0027@umn.edu</a></p>
                <p>&nbsp;</p></td>
              </tr>
              <tr>
                <td width="96" valign="top"><div align="center"><img src="students/pics/EllieEngelen.jpg" width="100" height="100" /></div></td>
                <td width="194" valign="top"><p><strong>Ellie Engelen</strong><br />
                  Verinary Medicine Student </p>                  </td>
                <td width="219" valign="top"><p><a href="mailto:engel536@umn.edu">engel536@umn.edu</a></p>                </td>
              </tr>
              <tr>
                <td width="96" valign="top"><div align="center"><img src="students/pics/TarissaLai.jpg" width="100" height="100" /></div></td>
                <td width="194" valign="top"><p><strong>Tarissa Lai</strong><br />
                  Medical Student </p>                  </td>
                <td width="219" valign="top"><p><a href="mailto:laixx149@umn.edu">laixx149@umn.edu</a></p>                </td>
              </tr>
              <tr>
                <td valign="top"><div align="center"><img src="students/pics/MariaSeewald.jpg" width="79" height="100" /></div></td>
                <td valign="top"><p><strong>Maria Seewald</strong><br />
                  Medical Student (University of <br />
                  Magdebury, Germany)</p>
                </td>
                <td valign="top"><p><a href="mailto:seewa010@umn.edu">seewa010@umn.edu</a><br />
                  <a href="mailto:maria.seewald@gmx.net">maria.seewald@gmx.net</a></p>
                </td>
              </tr>
              <tr>
                <td width="96" valign="top"><div align="center"><img src="students/pics/JerrodTembreull.jpg" width="100" height="100" /></div></td>
                <td width="194" valign="top"><p><strong>Jarrod Tembreull</strong><br />
                  Medical Student </p></td>
                <td width="219" valign="top"><p><a href="mailto:temb0006@umn.edu">temb0006@umn.edu</a></p></td>
              </tr>
              <tr>
                <td width="96" valign="top"><div align="center"><img src="students/pics/JeffTheismann.jpg" width="100" height="100" /></div></td>
                <td width="194" valign="top"><p><strong>Jeff Theismann</strong><br />
                  Medical Student </p>                </td>
                <td width="219" valign="top"><p><a href="mailto:theis312@umn.edu">theis312@umn.edu</a></p>                </td>
              </tr>
              <tr>
                <td width="96" valign="top"><div align="center"><img src="students/pics/KathrynThomas.jpg" width="100" height="100" /></div></td>
                <td width="194" valign="top"><p><strong>Kathryn Thomas</strong><br />
                  Medical Student<br />
                  CTSI Summer Program</p>                </td>
                <td width="219" valign="top"><p><a href="mailto:thom3793@umn.edu">thom3793@umn.edu</a><br />
                </p></td>
              </tr>
              <tr>
                <td width="96" valign="top"><div align="center"><img src="students/pics/MichaelTradewell.jpg" width="100" height="100" /></div></td>
                <td width="194" valign="top"><p><strong>Michael Tradewell</strong><br />
                  Medical Student</p>                </td>
                <td width="219" valign="top"><p><a href="mailto:trade011@umn.edu">trade011@umn.edu</a></p>                </td>
              </tr>
            </table>
    <p><a href="#top">return to top</a></p>
    <h2><br />
  <a name="volunteers" id="volunteers"></a> 
    Volunteers, Undergraduate Students, Casual/Temps/Directed Research </h2>
            <table border="1" cellpadding="2" cellspacing="0" class="vhlab_padded">
              <tr>
                <td width="100" valign="top"><img src="students/pics/BradyAnderson.jpg" width="100" height="100" /></td>
                <td width="200" valign="top"><p><strong>Brady Anderson</strong><br />
                  Volunteer (Biology/Kinesiology)</p>                </td>
                <td width="220" valign="top"><p><a href="mailto:and03257@umn.edu">and03257@umn.edu</a></p>                </td>
              </tr>
              <tr>
                <td width="100" valign="top"><img src="students/pics/ShancyAugustine.jpg" width="100" height="100" /></td>
                <td width="200" valign="top"><p><strong>Shancy Augustine</strong><br />
                Postdoctoral Volunteer </p>                </td>
                <td width="220" valign="top"><p><a href="mailto:shancyufl@gmail.com">shancyufl@gmail.com</a></p>                </td>
              </tr>
              <tr>
                <td valign="top"><div align="center"><img src="students/pics/LukasBaner.jpg" width="100" height="100" /></div></td>
                <td valign="top"><p><strong>Lukas Baner</strong><br />
                  Volunteer</p>
                </td>
                <td valign="top"><p><a href="mailto:lukaslp640@yahoo.com">lukaslp640@yahoo.com</a></p>
                </td>
              </tr>
              <tr>
                <td width="100" valign="top"><img src="students/pics/RachelBersie.jpg" width="100" height="100" /></td>
                <td width="200" valign="top"><p><strong>Rachel Bersie</strong><br />
                Volunteer (Pre-med) </p>                </td>
                <td width="220" valign="top"><p><a href="mailto:bers0041@umn.edu">bers0041@umn.edu</a></p>                </td>
              </tr>
              <tr>
                <td valign="top"><div align="center"><img src="students/pics/PaulCho.jpg" width="100" height="100" /></div></td>
                <td valign="top"><p><strong>Paul Cho</strong><br />
                  Volunteer (Physiology) </p>                  </td>
                <td valign="top"><p><a href="mailto:choxx500@umn.edu">choxx500@umn.edu</a></p>                </td>
              </tr>
              <tr>
                <td width="100" valign="top"><div align="center">Picture not <br />
                available</div></td>
                <td width="200" valign="top"><p><strong>Erik Donley</strong><br />
                  Casual/Temp</p>                </td>
                <td width="220" valign="top"><p><a href="mailto:donley.erik@gmail.com">donley.erik@gmail.com</a></p>                </td>
              </tr>
              <tr>
                <td width="100" valign="top"><img src="students/pics/AlecDonohue.jpg" width="100" height="100" /></td>
                <td width="200" valign="top"><p><strong>Alec Donohue</strong><br />
                Volunteer (Communications)</p>                  </td>
                <td width="220" valign="top"><p><a href="mailto:donoh084@umn.edu">donoh084@umn.edu</a></p>                </td>
              </tr>
              <tr>
                <td width="100" valign="top"><img src="students/pics/BradFredricksen.jpg" width="100" height="100" /></td>
                <td width="200" valign="top"><p><strong>Brad Fredrickson</strong><br />
                Volunteer (BMEn) </p>                  </td>
                <td width="220" valign="top"><p><a href="mailto:fredr294@umn.edu">fredr294@umn.edu</a></p>                </td>
              </tr>
              <tr>
                <td width="100" valign="top"><img src="students/pics/AllyFuher.jpg" width="100" height="100" /></td>
                <td width="200" valign="top"><p><strong>Ally Fuher </strong><br /> 
                Volunteer (Biology)</p>                </td>
                <td width="220" valign="top"><p><a href="mailto:fuher005@umn.edu">fuher005@umn.edu</a></p>                </td>
              </tr>
              <tr>
                <td valign="top"><div align="center"><img src="students/pics/EmmaGriebenow.jpg" width="100" height="100" /></div></td>
                <td valign="top"><p><strong>Emma Griebenow</strong><br />
                  Volunteer (Biology)
                    </p>                  </td>
                <td valign="top"><p><a href="mailto:grieb033@umn.edu">grieb033@umn.edu</a></p>                </td>
              </tr>
              <tr>
                <td valign="top"><div align="center"><img src="students/pics/AnneHaakenstad.jpg" width="100" height="100" /></div></td>
                <td valign="top"><p><strong>Annie Haakenstad</strong><br />
                  Volunteer (Neuroscience) </p>                  </td>
                <td valign="top"><p><a href="mailto:haake028@umn.edu">haake028@umn.edu</a></p>                </td>
              </tr>
              <tr>
                <td valign="top"><div align="center"><img src="students/pics/KevinHartoyo.jpg" width="100" height="100" /></div></td>
                <td valign="top"><p><strong>Kevin Hartoyo</strong><br />
                  Volunteer (BMEn)</p>                </td>
                <td valign="top"><p><a href="mailto:harto013@umn.edu">harto013@umn.edu</a></p>                </td>
              </tr>
              <tr>
                <td width="100" valign="top"><img src="students/pics/MackenzieHerzig.jpg" width="100" height="101" /></td>
                <td width="200" valign="top"><p><strong>Mackenzie Herzig</strong><br />
                Volunteer (Biology)</p>                  </td>
                <td width="220" valign="top"><p><a href="mailto:herzi014@umn.edu">herzi014@umn.edu</a></p>                </td>
              </tr>
              <tr>
                <td valign="top"><div align="center"><img src="students/pics/MartinKhoury.jpg" width="100" height="100" /></div></td>
                <td valign="top"><p><strong>Martin Khoury</strong><br />
                  Volunteer (Genetics &amp; Psychology)</p>                  </td>
                <td valign="top"><p><a href="mailto:khour015@umn.edu">khour015@umn.edu</a></p>                </td>
              </tr>
              <tr>
                <td width="100" valign="top"><img src="students/pics/KevinKriege.jpg" width="100" height="100" /></td>
                <td width="200" valign="top"><p><strong>Kevin Kriege</strong><br />
                  Volunteer (Physiology) </p>                  </td>
                <td width="220" valign="top"><p><a href="mailto:krie0208@umn.edu">krie0208@umn.edu</a></p>                </td>
              </tr>
              <tr>
                <td width="100" valign="top"><div align="center">Picture not <br />
                available</div></td>
                <td width="200" valign="top"><p><strong>Elizabeth Laakso</strong><br />
                Volunteer</p>                </td>
                <td width="220" valign="top"><p><a href="mailto:elaakso1996@gmail.com">elaakso1996@gmail.com</a></p>                </td>
              </tr>
              <tr>
                <td width="100" valign="top"><img src="students/pics/MelanieMenk.jpg" width="100" height="100" /></td>
                <td width="200" valign="top"><p><strong>Melanie Menk</strong><br />
                Volunteer (Biology)</p>                  </td>
                <td width="220" valign="top"><p><a href="mailto:menkx035@umn.edu">menkx035@umn.edu</a></p>                </td>
              </tr>
              <tr>
                <td width="100" valign="top"><img src="students/pics/NanaMitsuishi.jpg" width="100" height="100" /></td>
                <td width="200" valign="top"><p><strong>Nana Mitsuishi</strong><br />
                Volunteer (BMEn) </p>                </td>
                <td width="220" valign="top"><p><a href="mailto:mitsu009@umn.edu">mitsu009@umn.edu</a></p>                </td>
              </tr>
              <tr>
                <td width="100" valign="top"><img src="students/pics/SemalMusleh.jpg" width="100" height="100" /></td>
                <td width="200" valign="top"><p><strong>Semal Musleh</strong><br />
                Volunteer</p>                </td>
                <td width="220" valign="top"><p><a href="mailto:musl0006@umn.edu">musl0006@umn.edu</a><br />
                </p>                </td>
              </tr>
              <tr>
                <td width="100" valign="top"><img src="students/pics/SydneyNewton.jpg" width="100" height="100" /></td>
                <td width="200" valign="top"><p><strong>Sydney Newton</strong><br />
                Volunteer (Biology)</p>                  </td>
                <td width="220" valign="top"><p><a href="mailto:newto158@umn.edu">newto158@umn.edu</a><br />
                </p>                </td>
              </tr>
              <tr>
                <td width="100" valign="top"><img src="students/pics/CaseyRieck.jpg" width="100" height="100" /></td>
                <td width="200" valign="top"><p><strong>Casey Rieck</strong><br />
                Volunteer (Biology)</p>                  </td>
                <td width="220" valign="top"><p><a href="mailto:rieck057@umn.edu">rieck057@umn.edu</a></p>                </td>
              </tr>
              <tr>
                <td valign="top"><div align="center"><img src="students/pics/JakeSchauberger.jpg" width="100" height="100" /></div></td>
                <td valign="top"><p><strong>Jake Schauberger</strong><br />
                  Volunteer (Biochemistry)</p>                  </td>
                <td valign="top"><p><a href="mailto:schau290@umn.edu">schau290@umn.edu</a></p>                </td>
              </tr>
              <tr>
                <td width="100" valign="top"><img src="students/pics/KileySchmidt.jpg" width="100" height="100" /></td>
                <td width="200" valign="top"><p><strong>Kiley Schmidt</strong><br />
                  Casual/Temp</p>                  </td>
                <td width="220" valign="top"><p><a href="mailto:schm2687@umn.edu">schm2687@umn.edu</a></p>                </td>
              </tr>
              <tr>
                <td width="100" valign="top"><div align="center"><img src="students/pics/JerraldSpencer.jpg" width="79" height="100" /></div></td>
                <td width="200" valign="top"><p><strong>Jerrald Spencer </strong><br />
                Casual/Temp</p></td>
                <td width="220" valign="top"><p><a href="mailto:jdspence@umn.edu">jdspence@umn.edu</a></p></td>
              </tr>
    </table>
<a href="#top">return to top</a><br />
          		  </td>
<!-- InstanceEndEditable --></div>

  <!-- END CENTER COLUMN -->
</div>

<!--END TWO COLUMN PAGE CONTENT-->
<br class="clearabove" />


<!-- END PAGE CONTENT -->

<!-- BEGIN UofM FOOTER -->
<div class="grid_7 alpha" id="footer_inner">
   <ul class="copyright"><li>&copy; 2010 Regents of the University of Minnesota. All rights reserved.</li>
    <li>The University of Minnesota is an equal opportunity educator and employer</li>
    <li>Last modified on <!-- #BeginDate format:Am1 -->November 18, 2015<!-- #EndDate --></li></ul>
</div>
   <div class="grid_5 omega" id="footer_right">
    <ul class="footer_links">
    <li>Twin Cities Campus: </li>
    <li><a href="http://www1.umn.edu/pts/">Parking &amp; Transportation</a></li>
	<li><a href="http://www.umn.edu/twincities/maps/index.html">Maps &amp; Directions</a></li></ul>
    <br class="clearabove" />
    <ul class="footer_links"><li><a href="http://www.directory.umn.edu/">Directories</a></li>
    <li><a href="http://www.umn.edu/twincities/contact/">Contact U of M</a></li>
    <li><a href="http://www.privacy.umn.edu/">Privacy</a></li>
    </ul>
    <p>&nbsp;</p>
<br class="clearabove" />
</div>
<!-- END UofM FOOTER -->

</body>
<!-- InstanceEnd --></html>"""
    return HttpResponse(html)    
    
    
