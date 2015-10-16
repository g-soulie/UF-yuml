public class Team implements Competitor {
	private String name
	private <SingleCompetitor> members 
	
	public Team(String name){
	}

	public void add_member(SingleCompetitor member){
	}

	public void addMember(Competitor member){
	}

	public void deleteMember(Competitor member){
	}

	public boolean hasValidname(){
	}

	public  String get_name(){
		return name;
	}

	public  String set_name(String name){
		this.name=name;
	}

	public  <SingleCompetitor> get_members(){
		return members;
	}

	public  <SingleCompetitor> set_members(<SingleCompetitor> members){
		this.members=members;
	}
}