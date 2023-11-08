var sheet_id = "1VpjhqrUHi9BQGGktxSSj2lSO_fWQ23gnmul4Fz1aVrM";
var sheet_name = "attendance";
function doGet(e){
var ss = SpreadsheetApp.openById(sheet_id);
var sheet = ss.getSheetByName(sheet_name);
var Date = e.parameter.date;
var Time = e.parameter.time;
var Employee_ID = e.parameter.empid;
var Employee_Name = e.parameter.empname;
var Employee_Email_ID = e.parameter.empemail;
var Position = e.parameter.emppos;
var Punch_In_or_Out = e.parameter.emppio;
sheet.appendRow([Date,Time,Employee_ID,Employee_Name,Employee_Email_ID,Position,Punch_In_or_Out]);
}