public class Player {
    int number = 0;
    // String name;

        // public static void main() (String player_name) {
        //     name = (String) player_name;
        // }

        public void guess() {
            number = (int) (Math.random() * 10);
            System.out.println("Player says: I'm guessing " + number); 
        }

        public void cheat() {
            System.out.println("I'm cheating!");
        }
}
