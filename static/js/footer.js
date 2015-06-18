?// This is the common footer on all Heritage pages



document.writeln("<h6>Verse of the Day</h6>");
		
document.writeln("<script src='http://www.biblegateway.com/votd/votd.write.callback.js'></script>");

document.writeln("<script src='http://www.biblegateway.com/votd/get?format=json&amp;version=31&amp;callback=BG.votdWriteCallback'></script>");
		
document.writeln("<noscript>");
	document.writeln("<iframe id='gateway' src='http://www.biblegateway.com/votd/get?format=html&amp;version=NIV' seamless></iframe>");
document.writeln("</noscript>");
		
document.writeln("<br>");
document.writeln("<div id='rights'>");
	document.writeln("All rights reserved<br>");
	document.writeln("Created by WebMaster");
document.writeln("</div>");