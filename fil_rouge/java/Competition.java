public class Competition {
	private String name
	private Calendar closingDate
	private <Competitors> competitors
	private <Betting> bettings
	private <Competitor> podium
	private[' winner Competitor']
	
	public Competition(String name, Calendar closingDate){
	}

	public  String get_name(){
		return name;
	}

	public  String set_name(String name){
		this.name=name;
	}

	public  Calendar get_closingDate(){
		return closingDate;
	}

	public  Calendar set_closingDate(Calendar closingDate){
		this.closingDate=closingDate;
	}

	public  <Competitors> get_competitors(){
		return competitors;
	}

	public  <Competitors> set_competitors(<Competitors> competitors){
		this.competitors=competitors;
	}

	public  <Betting> get_bettings(){
		return bettings;
	}

	public  <Betting> set_bettings(<Betting> bettings){
		this.bettings=bettings;
	}

	public  <Competitor> get_podium(){
		return podium;
	}

	public  <Competitor> set_podium(<Competitor> podium){
		this.podium=podium;
	}
}