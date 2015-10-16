public class Team implements <<Competitor>> {
	private String  name
	private <SingleCompetitor>  members 
	
	public  Team(String name): void{
	}

	public  add_member(SingleCompetitor member): void{
	}

	public  addMember(Competitor member): void{
	}

	public  deleteMember(Competitor member): void{
	}

	public  hasValidname(): boolean{
	}
}