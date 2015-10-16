public class SingleCompetitor implements Competitor {
	private String last_name
	private String first_name
	private String borndate
	
	public SingleCompetitor(String last_name, String first_name, String borndate){
	}

	public void addMember(Competitor member){
	}

	public void deleteMember(Competitor member){
	}

	public boolean hasValidname(){
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
}