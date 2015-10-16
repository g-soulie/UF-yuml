public class Gestion implements Betting {
	
	void  addCompetition(java.lang.String competition, java.util.Calendar closingDate, java.util.Collection<Competitor> competitors, java.lang.String managerPwd) :void{
	}

	void  addCompetitor(java.lang.String competition, Competitor competitor, java.lang.String managerPwd){
	}

	void  authenticateMngr(java.lang.String managerPwd){
	}

	void  betOnPodium(long numberTokens, java.lang.String competition, Competitor winner, Competitor second, Competitor third, java.lang.String username, java.lang.String pwdSubs){
	}

	void  betOnWinner(long numberTokens, java.lang.String competition, Competitor winner, java.lang.String username, java.lang.String pwdSubs){
	}

	void  cancelCompetition(java.lang.String competition, java.lang.String managerPwd){
	}

	void  changeSubsPwd(java.lang.String username, java.lang.String newPwd, java.lang.String currentPwd){
	}

	java.util.ArrayList<java.lang.String>  consultBetsCompetition(java.lang.String competition){
	}

	java.util.ArrayList<Competitor>  consultResultsCompetition(java.lang.String competition){
	}

	Competitor  createCompetitor(java.lang.String name, java.lang.String managerPwd){
	}

	Competitor  createCompetitor(java.lang.String lastName, java.lang.String firstName, java.lang.String borndate, java.lang.String managerPwd){
	}

	void  creditSubscriber(java.lang.String username, long numberTokens, java.lang.String managerPwd){
	}

	void  debitSubscriber(java.lang.String username, long numberTokens, java.lang.String managerPwd){
	}

	void  deleteBetsCompetition(java.lang.String competition, java.lang.String username, java.lang.String pwdSubs){
	}

	void  deleteCompetition(java.lang.String competition, java.lang.String managerPwd){
	}

	void  deleteCompetitor(java.lang.String competition, Competitor competitor, java.lang.String managerPwd){
	}

	java.util.ArrayList<java.lang.String>  infosSubscriber(java.lang.String username, java.lang.String pwdSubs){
	}

	java.util.List<java.util.List<java.lang.String>>  listCompetitions(){
	}

	java.util.Collection<Competitor>  listCompetitors(java.lang.String competition){
	}

	java.util.List<java.util.List<java.lang.String>>  listSubscribers(java.lang.String managerPwd){
	}

	void  settlePodium(java.lang.String competition, Competitor winner, Competitor second, Competitor third, java.lang.String managerPwd){
	}

	void  settleWinner(java.lang.String competition, Competitor winner, java.lang.String managerPwd){
	}

	java.lang.String  subscribe(java.lang.String lastName, java.lang.String firstName, java.lang.String username, java.lang.String borndate, java.lang.String managerPwd){
	}

	long  unsubscribe(java.lang.String username, java.lang.String managerPwd){
	}
}