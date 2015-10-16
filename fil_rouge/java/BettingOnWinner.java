public class BettingOnWinner extends Betting {
	private Competitor winner
	private Subscriber subscriber
	private float amount
	private Competition competition
	
	public BettingOnWinner(Competitor winner){
	}

	public boolean prediction(Competitor winner){
	}

	public  Competitor get_winner(){
		return winner;
	}

	public  Competitor set_winner(Competitor winner){
		this.winner=winner;
	}

	public  Subscriber get_subscriber(){
		return subscriber;
	}

	public  Subscriber set_subscriber(Subscriber subscriber){
		this.subscriber=subscriber;
	}

	public  float get_amount(){
		return amount;
	}

	public  float set_amount(float amount){
		this.amount=amount;
	}

	public  Competition get_competition(){
		return competition;
	}

	public  Competition set_competition(Competition competition){
		this.competition=competition;
	}
}