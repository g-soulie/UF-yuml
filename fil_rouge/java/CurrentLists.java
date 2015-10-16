public class CurrentLists {
	private <team>  team
	private <Single_Competitor>  single_competitors
	private <Subscribers>  subscribers
	private <Competition>  current_Competitions
	private <Competition>  past_Competitions
	
	public  create_SingleCompetitor(java.lang.String lastName,java.lang.String firstName,java.lang.String borndate): Competitor{
	}

	public  create_Team(java.lang.String name): Competitor{
	}

	public  create_Competition(java.lang.String competition,java.util.Calendar closingDate,java.util.Collection<Competitor> competitors): Competition{
	}

	public  create_Subscriber(java.lang.String lastName,java.lang.String firstName,java.lang.String username,java.lang.String borndate): Subscriber{
	}
}