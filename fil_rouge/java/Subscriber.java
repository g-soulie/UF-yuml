public class Subscriber {
	private String last_name
	private String first_name
	private String borndate
	private String username
	private String pasword
	private float amount
	private <Betting> bettings
	
	public Subscriber(String last_name, String first_name, String username, String borndate){
	}

	public void add_bettingOnWinner(Competition competition, Competitor winner){
	}

	public void add_bettingOnPodium(Competition competition, Competitor first_winner, Competitor second_winner ,Competitor third_winner){
	}

	public  String get_last_name(){
		return last_name;
	}

	public  String set_last_name(String last_name){
		this.last_name=last_name;
	}

	public  String get_first_name(){
		return first_name;
	}

	public  String set_first_name(String first_name){
		this.first_name=first_name;
	}

	public  String get_borndate(){
		return borndate;
	}

	public  String set_borndate(String borndate){
		this.borndate=borndate;
	}

	public  String get_username(){
		return username;
	}

	public  String set_username(String username){
		this.username=username;
	}

	public  String get_pasword(){
		return pasword;
	}

	public  String set_pasword(String pasword){
		this.pasword=pasword;
	}

	public  float get_amount(){
		return amount;
	}

	public  float set_amount(float amount){
		this.amount=amount;
	}

	public  <Betting> get_bettings(){
		return bettings;
	}

	public  <Betting> set_bettings(<Betting> bettings){
		this.bettings=bettings;
	}
}