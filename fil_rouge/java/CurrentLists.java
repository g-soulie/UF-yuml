public class CurrentLists {
	private <team> team
	private <Single_Competitor> single_competitors
	private <Subscribers> subscribers
	private <Competition> current_Competitions
	private <Competition> past_Competitions
	
	public Competitor create_SingleCompetitor(java.lang.String lastName,java.lang.String firstName,java.lang.String borndate){
	}

	public Competitor create_Team(java.lang.String name){
	}

	public Competition create_Competition(java.lang.String competition,java.util.Calendar closingDate,java.util.Collection<Competitor> competitors){
	}

	public Subscriber create_Subscriber(java.lang.String lastName,java.lang.String firstName,java.lang.String username,java.lang.String borndate){
	}

	public  <team> get_team(){
		return team;
	}

	public  <team> set_team(<team> team){
		this.team=team;
	}

	public  <Single_Competitor> get_single_competitors(){
		return single_competitors;
	}

	public  <Single_Competitor> set_single_competitors(<Single_Competitor> single_competitors){
		this.single_competitors=single_competitors;
	}

	public  <Subscribers> get_subscribers(){
		return subscribers;
	}

	public  <Subscribers> set_subscribers(<Subscribers> subscribers){
		this.subscribers=subscribers;
	}

	public  <Competition> get_current_Competitions(){
		return current_Competitions;
	}

	public  <Competition> set_current_Competitions(<Competition> current_Competitions){
		this.current_Competitions=current_Competitions;
	}

	public  <Competition> get_past_Competitions(){
		return past_Competitions;
	}

	public  <Competition> set_past_Competitions(<Competition> past_Competitions){
		this.past_Competitions=past_Competitions;
	}
}