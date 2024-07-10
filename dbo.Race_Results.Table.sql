CREATE TABLE dbo.Race_Results
(
	Event_Year INT NOT NULL
	,Race_Number INT NOT NULL
	,Runner_Name VARCHAR(100) NOT NULL
	,Overall_Position INT
	,Finish_Time TIME 
	,Category VARCHAR(20) NOT NULL
	,Category_Position INT 
	,Gender VARCHAR(10) NOT NULL
	,Gender_Position INT
	,Club VARCHAR(100)
	,Country VARCHAR(50)	
	,Wave VARCHAR(10)	
	,Lynnfield_Park_Time TIME
	,Cato_Ridge_Time TIME	
	,Drummond_Time TIME	
	,Winston_Park_Time TIME	
	,Pinetown_Time TIME	
	,Sherwood_Time TIME	
	,PRIMARY KEY CLUSTERED (
		Event_Year
		,Race_Number
	)
)