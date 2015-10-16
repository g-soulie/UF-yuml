public class Subscriber {
	private String  last_name
	private String  first_name
	private String  borndate
	private String  username
	private String  pasword
	private float  amount
	private <Betting>  bettings
	
	public  Subscriber(String last_name, String first_name, String username, String borndate): void{
	}

	public  add_bettingOnWinner(Competition competition, Competitor winner): void{
	}

	public  add_bettingOnPodium(Competition competition, Competitor first_winner, Competitor second_winner ,Competitor third_winner): void{
	}
}