public interface Betting {
	public void addCompetition(String competition, Calendar closingDate, Collection<Competitor> competitors, String managerPwd){
	}

	public void addCompetitor(String competition, Competitor competitor, String managerPwd){
	}

	public void authenticateMngr(String managerPwd){
	}

	public void betOnPodium(long numberTokens, String competition, Competitor winner, Competitor second, Competitor third, String username, String pwdSubs){
	}

	public void betOnWinner(long numberTokens, String competition, Competitor winner, String username, String pwdSubs){
	}

	public void cancelCompetition(String competition, String managerPwd){
	}

	public void changeSubsPwd(String username, String newPwd, String currentPwd){
	}

	public ArrayList<String> consultBetsCompetition(String competition){
		return null;
	}

	public ArrayList<Competitor> consultResultsCompetition(String competition){
		return null;
	}

	public Competitor createCompetitor(String name, String managerPwd){
		return null;
	}

	public createCompetitor(String lastName, String firstName, String borndate, String managerPwd){
	}

	public void creditSubscriber(String username, long numberTokens, String managerPwd){
	}

	public void debitSubscriber(String username, long numberTokens, String managerPwd){
	}

	public void deleteBetsCompetition(String competition, String username, String pwdSubs){
	}

	public void deleteCompetition(String competition, String managerPwd){
	}

	public void deleteCompetitor(String competition, Competitor competitor, String managerPwd){
	}

	ArrayList<String> infosSubscriber(String username, String pwdSubs){
		return null;
	}

	public List<List<String>> listCompetitions(){
		return null;
	}

	public Collection<Competitor> listCompetitors(String competition){
		return null;
	}

	public List<List<String>> listSubscribers(String managerPwd){
		return null;
	}

	public void settlePodium(String competition, Competitor winner, Competitor second, Competitor third, String managerPwd){
	}

	public settleWinner(String competition, Competitor winner, String managerPwd){
	}

	void String  subscribe(String lastName, String firstName, String username, String borndate, String managerPwd){
	}

	public long unsubscribe(String username, String managerPwd){
		return 0;
	}


}