# ==============================================================================
# BREEDS SEED DATA
# ==============================================================================
# This file stores information about cat and dog breeds.
# The data is used by database.py to populate the 'breeds' table in SQLite.
#
# Every breed contains:
# - name: Breed name (title case, spaces instead of underscores)
# - animal: "Cat" or "Dog"
# - origin: Country of origin
# - lifespan: Typical lifespan range
# - size: "Small", "Medium", "Large", or "Giant"
# - temperament: Key personality traits
# - fun_fact: One interesting and accurate verified fact
# ==============================================================================

BREEDS_DATA = [
    # --------------------------------------------------------------------------
    # 12 CAT BREEDS (From Oxford-IIIT Pet Dataset)
    # --------------------------------------------------------------------------
    {
        "name": "Abyssinian",
        "animal": "Cat",
        "origin": "Ethiopia",
        "lifespan": "9-15 years",
        "size": "Medium",
        "temperament": "Curious, playful, active, intelligent",
        "fun_fact": "Known as the clown of the cat kingdom due to their playful antics."
    },
    {
        "name": "Bengal",
        "animal": "Cat",
        "origin": "United States",
        "lifespan": "12-16 years",
        "size": "Medium",
        "temperament": "Energetic, adventurous, affectionate, alert",
        "fun_fact": "Created by breeding domestic cats with the Asian leopard cat."
    },
    {
        "name": "Birman",
        "animal": "Cat",
        "origin": "Myanmar (Burma)",
        "lifespan": "12-16 years",
        "size": "Medium",
        "temperament": "Gentle, quiet, loving, patient",
        "fun_fact": "Also called the Sacred Cat of Burma, famous for distinct pure white paws called gloves."
    },
    {
        "name": "Bombay",
        "animal": "Cat",
        "origin": "United States",
        "lifespan": "12-16 years",
        "size": "Medium",
        "temperament": "Social, affectionate, intelligent, playful",
        "fun_fact": "Bred to look like a miniature black panther with striking copper eyes."
    },
    {
        "name": "British Shorthair",
        "animal": "Cat",
        "origin": "United Kingdom",
        "lifespan": "12-17 years",
        "size": "Medium",
        "temperament": "Calm, easygoing, loyal, dignified",
        "fun_fact": "The Cheshire Cat in Alice in Wonderland was inspired by the British Shorthair."
    },
    {
        "name": "Egyptian Mau",
        "animal": "Cat",
        "origin": "Egypt",
        "lifespan": "12-15 years",
        "size": "Medium",
        "temperament": "Fast, agile, loyal, observant",
        "fun_fact": "The fastest domestic cat breed, capable of running up to 30 mph (48 km/h)."
    },
    {
        "name": "Maine Coon",
        "animal": "Cat",
        "origin": "United States",
        "lifespan": "11-15 years",
        "size": "Large",
        "temperament": "Friendly, gentle giant, outgoing, sociable",
        "fun_fact": "One of the largest domestic cat breeds and known for their dog-like personalities."
    },
    {
        "name": "Persian",
        "animal": "Cat",
        "origin": "Iran",
        "lifespan": "12-17 years",
        "size": "Medium",
        "temperament": "Quiet, gentle, sweet, relaxed",
        "fun_fact": "Famous for their round flat faces, long luxurious fur, and calm presence."
    },
    {
        "name": "Ragdoll",
        "animal": "Cat",
        "origin": "United States",
        "lifespan": "12-17 years",
        "size": "Large",
        "temperament": "Docile, affectionate, relaxed, trusting",
        "fun_fact": "Named Ragdoll because they often go completely limp with joy when picked up."
    },
    {
        "name": "Russian Blue",
        "animal": "Cat",
        "origin": "Russia",
        "lifespan": "15-20 years",
        "size": "Medium",
        "temperament": "Reserved, gentle, quiet, loyal",
        "fun_fact": "Has a shimmering silver-tipped blue coat and vivid emerald green eyes."
    },
    {
        "name": "Siamese",
        "animal": "Cat",
        "origin": "Thailand",
        "lifespan": "12-18 years",
        "size": "Medium",
        "temperament": "Vocal, demanding, affectionate, social",
        "fun_fact": "One of the most talkative cat breeds with a distinctive loud meow."
    },
    {
        "name": "Sphynx",
        "animal": "Cat",
        "origin": "Canada",
        "lifespan": "12-16 years",
        "size": "Medium",
        "temperament": "Energetic, cuddly, curious, mischievous",
        "fun_fact": "Hairless due to a natural genetic mutation; feels like warm chamois leather to touch."
    },

    # --------------------------------------------------------------------------
    # 120+ DOG BREEDS (Stanford Dogs Dataset + Oxford-IIIT Pet Dog Breeds)
    # --------------------------------------------------------------------------
    {
        "name": "Affenpinscher",
        "animal": "Dog",
        "origin": "Germany",
        "lifespan": "12-15 years",
        "size": "Small",
        "temperament": "Confident, funny, stubborn, adventurous",
        "fun_fact": "Known as monkey terriers in Germany due to their primate-like facial expressions."
    },
    {
        "name": "Afghan Hound",
        "animal": "Dog",
        "origin": "Afghanistan",
        "lifespan": "12-14 years",
        "size": "Large",
        "temperament": "Aloof, dignified, independent, loyal",
        "fun_fact": "Ancient sighthound breed known for its flowing silky coat and curved tail."
    },
    {
        "name": "African Hunting Dog",
        "animal": "Dog",
        "origin": "Africa",
        "lifespan": "10-12 years",
        "size": "Medium",
        "temperament": "Social, cooperative, athletic, alert",
        "fun_fact": "Also called the African Wild Dog, famous for its colorful calico-patterned coat."
    },
    {
        "name": "Airedale",
        "animal": "Dog",
        "origin": "United Kingdom",
        "lifespan": "11-14 years",
        "size": "Large",
        "temperament": "Clever, confident, friendly, outgoing",
        "fun_fact": "Known as the 'King of Terriers' because it is the largest of all terrier breeds."
    },
    {
        "name": "American Bulldog",
        "animal": "Dog",
        "origin": "United States",
        "lifespan": "10-14 years",
        "size": "Large",
        "temperament": "Confident, loyal, assertive, protective",
        "fun_fact": "Originally bred for farm work and catching feral cattle and wild boars."
    },
    {
        "name": "American Pit Bull Terrier",
        "animal": "Dog",
        "origin": "United States",
        "lifespan": "12-16 years",
        "size": "Medium",
        "temperament": "Courageous, affectionate, playful, determined",
        "fun_fact": "Known for having great athleticism and an extraordinarily loyal bond with family."
    },
    {
        "name": "American Staffordshire Terrier",
        "animal": "Dog",
        "origin": "United States",
        "lifespan": "12-16 years",
        "size": "Medium",
        "temperament": "Confident, smart, good-natured, loyal",
        "fun_fact": "A decorated military war dog named Sergeant Stubby was famously of this lineage."
    },
    {
        "name": "Appenzeller",
        "animal": "Dog",
        "origin": "Switzerland",
        "lifespan": "12-15 years",
        "size": "Medium",
        "temperament": "Agile, enthusiastic, intelligent, watchful",
        "fun_fact": "One of four Swiss Sennenhund cattle-herding dogs, recognized by its curled ring tail."
    },
    {
        "name": "Australian Terrier",
        "animal": "Dog",
        "origin": "Australia",
        "lifespan": "12-15 years",
        "size": "Small",
        "temperament": "Spirited, alert, courageous, friendly",
        "fun_fact": "First native Australian dog breed to be recognized and shown in kennel clubs."
    },
    {
        "name": "Basenji",
        "animal": "Dog",
        "origin": "Democratic Republic of the Congo",
        "lifespan": "12-14 years",
        "size": "Small",
        "temperament": "Quiet, independent, curious, energetic",
        "fun_fact": "Known as the barkless dog; instead of barking, it produces a unique sound like a yodel."
    },
    {
        "name": "Basset Hound",
        "animal": "Dog",
        "origin": "France",
        "lifespan": "10-12 years",
        "size": "Medium",
        "temperament": "Gentle, relaxed, patient, scent-driven",
        "fun_fact": "Their long droopy ears help sweep scents from the ground directly toward their nose."
    },
    {
        "name": "Beagle",
        "animal": "Dog",
        "origin": "United Kingdom",
        "lifespan": "12-15 years",
        "size": "Small",
        "temperament": "Friendly, curious, merry, determined",
        "fun_fact": "Snoopy from the famous Peanuts comic strip is the world's most famous Beagle."
    },
    {
        "name": "Bearded Collie",
        "animal": "Dog",
        "origin": "Scotland",
        "lifespan": "12-14 years",
        "size": "Medium",
        "temperament": "Bouncy, lively, charismatic, alert",
        "fun_fact": "Affectionately called 'Beardie', known for performing a signature jumping bounce."
    },
    {
        "name": "Beauceron",
        "animal": "Dog",
        "origin": "France",
        "lifespan": "10-12 years",
        "size": "Large",
        "temperament": "Loyal, courageous, calm, obedient",
        "fun_fact": "Has distinctive double dewclaws on its hind legs used for traction in rough terrain."
    },
    {
        "name": "Bedlington Terrier",
        "animal": "Dog",
        "origin": "United Kingdom",
        "lifespan": "12-14 years",
        "size": "Small",
        "temperament": "Gentle, spirited, intelligent, affectionate",
        "fun_fact": "Looks like a little lamb due to its unique curved back and pear-shaped curly head."
    },
    {
        "name": "Belgian Malinois",
        "animal": "Dog",
        "origin": "Belgium",
        "lifespan": "12-14 years",
        "size": "Large",
        "temperament": "Intelligent, hardworking, vigilant, protective",
        "fun_fact": "Highly favored worldwide as premier military and police detection dogs."
    },
    {
        "name": "Belgian Sheepdog",
        "animal": "Dog",
        "origin": "Belgium",
        "lifespan": "12-14 years",
        "size": "Large",
        "temperament": "Alert, loyal, sensitive, devoted",
        "fun_fact": "Distinguished by an all-black double coat and exceptional trainability."
    },
    {
        "name": "Belgian Tervuren",
        "animal": "Dog",
        "origin": "Belgium",
        "lifespan": "12-14 years",
        "size": "Large",
        "temperament": "Courageous, active, intelligent, possessive",
        "fun_fact": "Recognized for a rich fawn-to-russet long coat with blackened tips."
    },
    {
        "name": "Bernese Mountain Dog",
        "animal": "Dog",
        "origin": "Switzerland",
        "lifespan": "7-10 years",
        "size": "Large",
        "temperament": "Affectionate, patient, calm, gentle",
        "fun_fact": "Originally served Swiss dairy farmers by pulling heavy carts of milk and cheese."
    },
    {
        "name": "Bichon Frise",
        "animal": "Dog",
        "origin": "Spain / France",
        "lifespan": "12-15 years",
        "size": "Small",
        "temperament": "Playful, cheery, gentle, affectionate",
        "fun_fact": "Popular with European royalty in the Renaissance as pampering lapdogs."
    },
    {
        "name": "Black And Tan Coonhound",
        "animal": "Dog",
        "origin": "United States",
        "lifespan": "10-12 years",
        "size": "Large",
        "temperament": "Easygoing, tenacious, friendly, melodic bark",
        "fun_fact": "Descended from Bloodhounds and Foxhounds to trail raccoons by night."
    },
    {
        "name": "Blenheim Spaniel",
        "animal": "Dog",
        "origin": "United Kingdom",
        "lifespan": "10-14 years",
        "size": "Small",
        "temperament": "Affectionate, graceful, sweet, gentle",
        "fun_fact": "Named after Blenheim Palace, ancestral home of the Dukes of Marlborough."
    },
    {
        "name": "Bloodhound",
        "animal": "Dog",
        "origin": "France / Belgium",
        "lifespan": "10-12 years",
        "size": "Large",
        "temperament": "Stubborn, gentle, patient, scent-master",
        "fun_fact": "Their sense of smell is so reliable that trail evidence is admissible in court."
    },
    {
        "name": "Border Collie",
        "animal": "Dog",
        "origin": "United Kingdom",
        "lifespan": "12-15 years",
        "size": "Medium",
        "temperament": "Highly intelligent, energetic, responsive, alert",
        "fun_fact": "Widely ranked as the most intelligent and trainable dog breed in the world."
    },
    {
        "name": "Border Terrier",
        "animal": "Dog",
        "origin": "United Kingdom",
        "lifespan": "12-15 years",
        "size": "Small",
        "temperament": "Even-tempered, plucky, affectionate, curious",
        "fun_fact": "Has an otter-shaped head and a harsh, weather-resistant double coat."
    },
    {
        "name": "Borzoi",
        "animal": "Dog",
        "origin": "Russia",
        "lifespan": "10-12 years",
        "size": "Large",
        "temperament": "Gentle, graceful, quiet, athletic",
        "fun_fact": "Formerly bred by Russian Tsars to hunt wolves across vast open plains."
    },
    {
        "name": "Boston Bull",
        "animal": "Dog",
        "origin": "United States",
        "lifespan": "11-14 years",
        "size": "Small",
        "temperament": "Friendly, lively, adaptable, polite",
        "fun_fact": "Known as the 'American Gentleman' because of its tuxedo-like black and white coat."
    },
    {
        "name": "Bouvier Des Flandres",
        "animal": "Dog",
        "origin": "Belgium / France",
        "lifespan": "10-12 years",
        "size": "Large",
        "temperament": "Gentle, loyal, brave, industrious",
        "fun_fact": "Its name translates to 'Cow Herder of Flanders' in French."
    },
    {
        "name": "Boxer",
        "animal": "Dog",
        "origin": "Germany",
        "lifespan": "10-12 years",
        "size": "Large",
        "temperament": "Playful, high-energy, friendly, protective",
        "fun_fact": "Named because they often stand on hind legs and bat with front paws during play."
    },
    {
        "name": "Brabancon Griffon",
        "animal": "Dog",
        "origin": "Belgium",
        "lifespan": "12-15 years",
        "size": "Small",
        "temperament": "Proud, sensitive, alert, lively",
        "fun_fact": "The smooth-coated variety of Brussels Griffon with nearly human facial expressions."
    },
    {
        "name": "Briard",
        "animal": "Dog",
        "origin": "France",
        "lifespan": "10-12 years",
        "size": "Large",
        "temperament": "Faithful, smart, brave, watchful",
        "fun_fact": "Thomas Jefferson fell in love with Briards while serving as diplomat in France."
    },
    {
        "name": "Brittany Spaniel",
        "animal": "Dog",
        "origin": "France",
        "lifespan": "12-14 years",
        "size": "Medium",
        "temperament": "Agile, quick, happy, eager to please",
        "fun_fact": "Named after the northwestern French province of Brittany."
    },
    {
        "name": "Bull Mastiff",
        "animal": "Dog",
        "origin": "United Kingdom",
        "lifespan": "8-10 years",
        "size": "Giant",
        "temperament": "Docile, reliable, protective, calm",
        "fun_fact": "Bred by gamekeepers to pin down poachers without biting them."
    },
    {
        "name": "Cairn",
        "animal": "Dog",
        "origin": "Scotland",
        "lifespan": "13-15 years",
        "size": "Small",
        "temperament": "Spirited, resilient, cheerful, independent",
        "fun_fact": "Toto from The Wizard of Oz was a Cairn Terrier named Terry."
    },
    {
        "name": "Cardigan",
        "animal": "Dog",
        "origin": "Wales, United Kingdom",
        "lifespan": "12-15 years",
        "size": "Medium",
        "temperament": "Affectionate, loyal, smart, active",
        "fun_fact": "Distinguished from Pembroke corgis by their long, bushy fox-like tails."
    },
    {
        "name": "Chesapeake Bay Retriever",
        "animal": "Dog",
        "origin": "United States",
        "lifespan": "10-13 years",
        "size": "Large",
        "temperament": "Affectionate, hardworking, courageous, protective",
        "fun_fact": "Possesses a naturally oily water-repellent coat that sheds icy river water."
    },
    {
        "name": "Chihuahua",
        "animal": "Dog",
        "origin": "Mexico",
        "lifespan": "14-18 years",
        "size": "Small",
        "temperament": "Graceful, sassy, alert, devoted",
        "fun_fact": "The smallest recognized dog breed in the world, named after the Mexican state of Chihuahua."
    },
    {
        "name": "Chow",
        "animal": "Dog",
        "origin": "China",
        "lifespan": "9-12 years",
        "size": "Medium",
        "temperament": "Dignified, aloof, clean, loyal",
        "fun_fact": "Famous for its unique blue-black tongue and lion-like mane."
    },
    {
        "name": "Clumber",
        "animal": "Dog",
        "origin": "United Kingdom",
        "lifespan": "10-12 years",
        "size": "Large",
        "temperament": "Gentle, calm, thoughtful, steady",
        "fun_fact": "The heaviest of all spaniel breeds, nicknamed the 'quiet gentleman' of gundogs."
    },
    {
        "name": "Cocker Spaniel",
        "animal": "Dog",
        "origin": "United Kingdom / United States",
        "lifespan": "10-14 years",
        "size": "Small",
        "temperament": "Gentle, smart, happy, affectionate",
        "fun_fact": "Named because they were bred to hunt the woodcock bird in English brush."
    },
    {
        "name": "Collie",
        "animal": "Dog",
        "origin": "Scotland",
        "lifespan": "12-14 years",
        "size": "Large",
        "temperament": "Devoted, graceful, intelligent, gentle",
        "fun_fact": "Immortalized in television history as the heroic rescue dog Lassie."
    },
    {
        "name": "Curly-Coated Retriever",
        "animal": "Dog",
        "origin": "United Kingdom",
        "lifespan": "10-12 years",
        "size": "Large",
        "temperament": "Confident, proud, independent, intelligent",
        "fun_fact": "One of the oldest retriever breeds, covered in crisp, small water-resistant curls."
    },
    {
        "name": "Dhole",
        "animal": "Dog",
        "origin": "Central & South Asia",
        "lifespan": "10-13 years",
        "size": "Medium",
        "temperament": "Social, communicative, agile, athletic",
        "fun_fact": "Also called the Asiatic wild dog, known to make high-pitched whistling calls."
    },
    {
        "name": "Dingo",
        "animal": "Dog",
        "origin": "Australia",
        "lifespan": "12-15 years",
        "size": "Medium",
        "temperament": "Independent, shy, alert, agile",
        "fun_fact": "Australia's native wild canine that has lived on the continent for over 4,000 years."
    },
    {
        "name": "Doberman",
        "animal": "Dog",
        "origin": "Germany",
        "lifespan": "10-12 years",
        "size": "Large",
        "temperament": "Fearless, alert, loyal, highly trainable",
        "fun_fact": "First bred by tax collector Louis Dobermann to protect him while carrying cash."
    },
    {
        "name": "English Cocker Spaniel",
        "animal": "Dog",
        "origin": "United Kingdom",
        "lifespan": "12-15 years",
        "size": "Medium",
        "temperament": "Affectionate, friendly, playful, faithful",
        "fun_fact": "Known as the 'merry cocker' because their tail wags almost constantly."
    },
    {
        "name": "English Foxhound",
        "animal": "Dog",
        "origin": "United Kingdom",
        "lifespan": "10-13 years",
        "size": "Large",
        "temperament": "Gentle, active, pack-oriented, athletic",
        "fun_fact": "Bred for stamina to run alongside horses for miles during traditional hunts."
    },
    {
        "name": "English Setter",
        "animal": "Dog",
        "origin": "United Kingdom",
        "lifespan": "11-14 years",
        "size": "Large",
        "temperament": "Sweet, quiet, friendly, energetic outdoors",
        "fun_fact": "Known for distinctive speckling in its silky coat, termed 'belton'."
    },
    {
        "name": "English Springer",
        "animal": "Dog",
        "origin": "United Kingdom",
        "lifespan": "12-14 years",
        "size": "Medium",
        "temperament": "Eager to please, cheerful, energetic, gentle",
        "fun_fact": "Named for springing game into the air for bird hunters."
    },
    {
        "name": "Entlebucher",
        "animal": "Dog",
        "origin": "Switzerland",
        "lifespan": "11-13 years",
        "size": "Medium",
        "temperament": "Agile, confident, cheerful, protective",
        "fun_fact": "The smallest of the four famous Swiss Mountain Dogs."
    },
    {
        "name": "Eskimo Dog",
        "animal": "Dog",
        "origin": "Arctic / Canada",
        "lifespan": "10-14 years",
        "size": "Large",
        "temperament": "Hardworking, loyal, courageous, quiet",
        "fun_fact": "Thrived in freezing Arctic conditions pulling heavy sledges for thousands of years."
    },
    {
        "name": "Flat-Coated Retriever",
        "animal": "Dog",
        "origin": "United Kingdom",
        "lifespan": "8-10 years",
        "size": "Large",
        "temperament": "Forever young, optimistic, energetic, devoted",
        "fun_fact": "Called the Peter Pan of dogs because it retains puppy-like enthusiasm for life."
    },
    {
        "name": "French Bulldog",
        "animal": "Dog",
        "origin": "France",
        "lifespan": "10-12 years",
        "size": "Small",
        "temperament": "Affectionate, easygoing, patient, playful",
        "fun_fact": "Famous for their distinctive bat ears and quiet, apartment-friendly disposition."
    },
    {
        "name": "German Shepherd",
        "animal": "Dog",
        "origin": "Germany",
        "lifespan": "9-13 years",
        "size": "Large",
        "temperament": "Courageous, intelligent, loyal, watchful",
        "fun_fact": "Renowned across the globe as top guide, search-and-rescue, and service dogs."
    },
    {
        "name": "German Shorthaired",
        "animal": "Dog",
        "origin": "Germany",
        "lifespan": "10-12 years",
        "size": "Large",
        "temperament": "Enthusiastic, bold, smart, cooperative",
        "fun_fact": "Features webbed feet that make them exceptional swimmers in rivers and lakes."
    },
    {
        "name": "Giant Schnauzer",
        "animal": "Dog",
        "origin": "Germany",
        "lifespan": "10-12 years",
        "size": "Large",
        "temperament": "Alert, loyal, spirited, imposing",
        "fun_fact": "Features iconic walrus-style beards and bushy eyebrows that shield their eyes."
    },
    {
        "name": "Golden Retriever",
        "animal": "Dog",
        "origin": "Scotland",
        "lifespan": "10-12 years",
        "size": "Large",
        "temperament": "Intelligent, friendly, devoted, reliable",
        "fun_fact": "Famous for having soft mouths, capable of holding an egg gently without breaking it."
    },
    {
        "name": "Gordon Setter",
        "animal": "Dog",
        "origin": "Scotland",
        "lifespan": "11-13 years",
        "size": "Large",
        "temperament": "Confident, affectionate, loyal, fearless",
        "fun_fact": "Developed at Gordon Castle by the Fourth Duke of Gordon in the Scottish highlands."
    },
    {
        "name": "Great Dane",
        "animal": "Dog",
        "origin": "Germany",
        "lifespan": "7-10 years",
        "size": "Giant",
        "temperament": "Friendly, patient, dependable, gentle",
        "fun_fact": "Known as the Apollo of dogs; holds multiple Guinness records for the tallest dog ever."
    },
    {
        "name": "Great Pyrenees",
        "animal": "Dog",
        "origin": "Pyrenees Mountains (France/Spain)",
        "lifespan": "10-12 years",
        "size": "Giant",
        "temperament": "Patient, calm, brave, gentle guardian",
        "fun_fact": "Historically appointed as the Royal Dog of France in the court of King Louis XIV."
    },
    {
        "name": "Greater Swiss Mountain Dog",
        "animal": "Dog",
        "origin": "Switzerland",
        "lifespan": "8-11 years",
        "size": "Giant",
        "temperament": "Faithful, alert, calm, strong",
        "fun_fact": "Nicknamed 'Swissy', historically pulled wagons for Swiss farmers and cheese makers."
    },
    {
        "name": "Groenendael",
        "animal": "Dog",
        "origin": "Belgium",
        "lifespan": "12-14 years",
        "size": "Large",
        "temperament": "Intelligent, vigilant, protective, affectionate",
        "fun_fact": "Also known as the black Belgian Sheepdog, named after the village of Groenendael."
    },
    {
        "name": "Havanese",
        "animal": "Dog",
        "origin": "Cuba",
        "lifespan": "14-16 years",
        "size": "Small",
        "temperament": "Playful, affectionate, gentle, sociable",
        "fun_fact": "The national dog of Cuba and the island's only native dog breed."
    },
    {
        "name": "Ibizan Hound",
        "animal": "Dog",
        "origin": "Spain (Balearic Islands)",
        "lifespan": "11-14 years",
        "size": "Large",
        "temperament": "Even-tempered, playful, athletic, independent",
        "fun_fact": "Can jump up to 6 feet in the air from a complete standstill."
    },
    {
        "name": "Irish Setter",
        "animal": "Dog",
        "origin": "Ireland",
        "lifespan": "12-14 years",
        "size": "Large",
        "temperament": "Outgoing, high-spirited, affectionate, playful",
        "fun_fact": "Renowned for its gleaming, flame-red chestnut coat and rollover friendly personality."
    },
    {
        "name": "Irish Terrier",
        "animal": "Dog",
        "origin": "Ireland",
        "lifespan": "12-15 years",
        "size": "Medium",
        "temperament": "Bold, spirited, tender-hearted, courageous",
        "fun_fact": "Served as fearless message couriers in the trenches during World War I."
    },
    {
        "name": "Irish Water Spaniel",
        "animal": "Dog",
        "origin": "Ireland",
        "lifespan": "11-13 years",
        "size": "Large",
        "temperament": "Playful, intelligent, inquisitive, alert",
        "fun_fact": "Features a unique smooth 'rat tail' that contrasts with its dense curly coat."
    },
    {
        "name": "Irish Wolfhound",
        "animal": "Dog",
        "origin": "Ireland",
        "lifespan": "6-8 years",
        "size": "Giant",
        "temperament": "Gentle, noble, patient, sensitive",
        "fun_fact": "Historically used in Ireland to hunt elk and wolves; among the tallest dog breeds."
    },
    {
        "name": "Italian Greyhound",
        "animal": "Dog",
        "origin": "Italy",
        "lifespan": "13-15 years",
        "size": "Small",
        "temperament": "Sensitive, affectionate, graceful, athletic",
        "fun_fact": "A cherished companion of European noblewomen, weighing just 7 to 14 pounds."
    },
    {
        "name": "Japanese Chin",
        "animal": "Dog",
        "origin": "Japan",
        "lifespan": "10-14 years",
        "size": "Small",
        "temperament": "Charming, loving, cat-like, aristocratic",
        "fun_fact": "Often behaves like a cat: washes its face with paws and perches on high cushions."
    },
    {
        "name": "Keeshond",
        "animal": "Dog",
        "origin": "Netherlands",
        "lifespan": "12-15 years",
        "size": "Medium",
        "temperament": "Outgoing, affectionate, friendly, quick to learn",
        "fun_fact": "Served as barge watchdogs in Holland and wear distinctive dark 'spectacles' around their eyes."
    },
    {
        "name": "Kelpie",
        "animal": "Dog",
        "origin": "Australia",
        "lifespan": "12-15 years",
        "size": "Medium",
        "temperament": "Tireless, loyal, smart, workaholic",
        "fun_fact": "Famous in the Australian outback for running across the backs of sheep in crowded pens."
    },
    {
        "name": "Kerry Blue Terrier",
        "animal": "Dog",
        "origin": "Ireland",
        "lifespan": "12-15 years",
        "size": "Medium",
        "temperament": "Smart, loyal, humorous, watchful",
        "fun_fact": "Puppies are born jet black and gradually turn into a striking slate blue by age two."
    },
    {
        "name": "Komondor",
        "animal": "Dog",
        "origin": "Hungary",
        "lifespan": "10-12 years",
        "size": "Large",
        "temperament": "Calm, brave, independent, devoted",
        "fun_fact": "Famous for long white corded fur resembling a mop, which protected them from wolves."
    },
    {
        "name": "Kuvasz",
        "animal": "Dog",
        "origin": "Hungary",
        "lifespan": "10-12 years",
        "size": "Large",
        "temperament": "Protective, patient, dignified, intelligent",
        "fun_fact": "Ancient flock protector whose snow-white coat allowed shepherds to spot it among sheep at night."
    },
    {
        "name": "Labrador Retriever",
        "animal": "Dog",
        "origin": "Canada (Newfoundland)",
        "lifespan": "11-13 years",
        "size": "Large",
        "temperament": "Friendly, active, outgoing, gentle",
        "fun_fact": "Held the title of America's most popular dog breed for an unprecedented 31 consecutive years."
    },
    {
        "name": "Lakeland Terrier",
        "animal": "Dog",
        "origin": "United Kingdom",
        "lifespan": "12-15 years",
        "size": "Small",
        "temperament": "Bold, confident, friendly, playful",
        "fun_fact": "Bred in England's rugged Lake District to protect sheep flocks from mountain foxes."
    },
    {
        "name": "Leonberger",
        "animal": "Dog",
        "origin": "Germany",
        "lifespan": "8-10 years",
        "size": "Giant",
        "temperament": "Gentle, friendly, playful, calm",
        "fun_fact": "Bred to resemble the lion in the crest of the city of Leonberg, Germany."
    },
    {
        "name": "Lhasa",
        "animal": "Dog",
        "origin": "Tibet",
        "lifespan": "12-15 years",
        "size": "Small",
        "temperament": "Playful, confident, devoted, vigilant",
        "fun_fact": "Served as sacred inside sentinels within Tibetan monasteries and palaces."
    },
    {
        "name": "Malamute",
        "animal": "Dog",
        "origin": "Alaska, United States",
        "lifespan": "10-14 years",
        "size": "Large",
        "temperament": "Friendly, playful, devoted, loyal",
        "fun_fact": "Bred by the Mahlemut Inuit tribe to pull heavy freight sleds over great snowy distances."
    },
    {
        "name": "Malinois",
        "animal": "Dog",
        "origin": "Belgium",
        "lifespan": "12-14 years",
        "size": "Large",
        "temperament": "Hardworking, confident, affectionate, active",
        "fun_fact": "World famous for jumping hurdles over 8 feet tall and detecting complex odors."
    },
    {
        "name": "Maltese Dog",
        "animal": "Dog",
        "origin": "Malta",
        "lifespan": "12-15 years",
        "size": "Small",
        "temperament": "Gentle, playful, charming, affectionate",
        "fun_fact": "Known as the 'Ye Ancient Dogge of Malta', praised by Aristotle in ancient Greece."
    },
    {
        "name": "Mexican Hairless",
        "animal": "Dog",
        "origin": "Mexico",
        "lifespan": "12-15 years",
        "size": "Medium",
        "temperament": "Calm, alert, loyal, peaceful",
        "fun_fact": "Also called the Xoloitzcuintli, revered by ancient Aztecs as sacred spiritual guardians."
    },
    {
        "name": "Miniature Pinscher",
        "animal": "Dog",
        "origin": "Germany",
        "lifespan": "12-16 years",
        "size": "Small",
        "temperament": "Fearless, spirited, assertive, quick",
        "fun_fact": "Nicknamed the 'King of Toys', known for a distinctive high-stepping hackney gait."
    },
    {
        "name": "Miniature Poodle",
        "animal": "Dog",
        "origin": "France / Germany",
        "lifespan": "13-16 years",
        "size": "Small",
        "temperament": "Intelligent, lively, alert, trainable",
        "fun_fact": "Ranked second only to the Border Collie in canine intelligence and agility."
    },
    {
        "name": "Miniature Schnauzer",
        "animal": "Dog",
        "origin": "Germany",
        "lifespan": "12-15 years",
        "size": "Small",
        "temperament": "Friendly, smart, obedient, alert",
        "fun_fact": "Has distinctive bushy eyebrows and beard, bred as farm rat catchers."
    },
    {
        "name": "Newfoundland",
        "animal": "Dog",
        "origin": "Canada",
        "lifespan": "9-11 years",
        "size": "Giant",
        "temperament": "Sweet, patient, devoted, gentle",
        "fun_fact": "Famous for webbed feet and a thick waterproof coat that makes them legendary water rescuers."
    },
    {
        "name": "Norfolk Terrier",
        "animal": "Dog",
        "origin": "United Kingdom",
        "lifespan": "12-15 years",
        "size": "Small",
        "temperament": "Fearless, affectionate, sociable, lively",
        "fun_fact": "Distinguished from the Norwich terrier by its folded drop ears instead of prick ears."
    },
    {
        "name": "Norwegian Elkhound",
        "animal": "Dog",
        "origin": "Norway",
        "lifespan": "12-15 years",
        "size": "Medium",
        "temperament": "Bold, playful, friendly, alert",
        "fun_fact": "Ancient companion of the Vikings, who sailed with them on longships."
    },
    {
        "name": "Norwich Terrier",
        "animal": "Dog",
        "origin": "United Kingdom",
        "lifespan": "12-15 years",
        "size": "Small",
        "temperament": "Affectionate, inquisitive, energetic, hardy",
        "fun_fact": "Famous for its upright, pointed ears and spirited fox-like expression."
    },
    {
        "name": "Old English Sheepdog",
        "animal": "Dog",
        "origin": "United Kingdom",
        "lifespan": "10-12 years",
        "size": "Large",
        "temperament": "Adaptable, gentle, intelligent, playful",
        "fun_fact": "Known as the 'Bobtail' because historically their tails were docked for identification."
    },
    {
        "name": "Otterhound",
        "animal": "Dog",
        "origin": "United Kingdom",
        "lifespan": "10-13 years",
        "size": "Large",
        "temperament": "Amiable, boisterous, even-tempered, athletic",
        "fun_fact": "One of the rarest dog breeds in the world, equipped with webbed paws for swimming."
    },
    {
        "name": "Papillon",
        "animal": "Dog",
        "origin": "France",
        "lifespan": "13-16 years",
        "size": "Small",
        "temperament": "Happy, alert, friendly, quick",
        "fun_fact": "Papillon means 'butterfly' in French, named for its wing-like fringed ears."
    },
    {
        "name": "Pekinese",
        "animal": "Dog",
        "origin": "China",
        "lifespan": "12-14 years",
        "size": "Small",
        "temperament": "Affectionate, regal, stubborn, courageous",
        "fun_fact": "Ancient imperial lapdog of Chinese emperors; only royals were allowed to own them."
    },
    {
        "name": "Pembroke",
        "animal": "Dog",
        "origin": "Wales, United Kingdom",
        "lifespan": "12-14 years",
        "size": "Small",
        "temperament": "Outgoing, smart, playful, affectionate",
        "fun_fact": "The royal favorite of Queen Elizabeth II, who owned over 30 Pembroke Welsh Corgis."
    },
    {
        "name": "Pomeranian",
        "animal": "Dog",
        "origin": "Pomerania (Germany/Poland)",
        "lifespan": "12-16 years",
        "size": "Small",
        "temperament": "Extroverted, lively, intelligent, curious",
        "fun_fact": "Despite weighing only 3 to 7 pounds, they descend from much larger Arctic sled dogs."
    },
    {
        "name": "Pug",
        "animal": "Dog",
        "origin": "China",
        "lifespan": "12-15 years",
        "size": "Small",
        "temperament": "Charming, mischievous, loving, docile",
        "fun_fact": "A group of pugs is officially called a 'grumble'."
    },
    {
        "name": "Redbone",
        "animal": "Dog",
        "origin": "United States",
        "lifespan": "11-13 years",
        "size": "Large",
        "temperament": "Even-tempered, energetic, gentle, eager",
        "fun_fact": "Famous for its stunning solid red coat and featured in the classic novel 'Where the Red Fern Grows'."
    },
    {
        "name": "Rhodesian Ridgeback",
        "animal": "Dog",
        "origin": "Zimbabwe / South Africa",
        "lifespan": "10-12 years",
        "size": "Large",
        "temperament": "Dignified, intelligent, athletic, loyal",
        "fun_fact": "Named for a distinct stripe of hair along its spine that grows backwards against the coat."
    },
    {
        "name": "Rottweiler",
        "animal": "Dog",
        "origin": "Germany",
        "lifespan": "9-11 years",
        "size": "Large",
        "temperament": "Loyal, loving, confident guardian, calm",
        "fun_fact": "Roman legions used early Rottweilers to herd livestock along military campaigns."
    },
    {
        "name": "Saint Bernard",
        "animal": "Dog",
        "origin": "Switzerland / Italy",
        "lifespan": "8-10 years",
        "size": "Giant",
        "temperament": "Gentle, friendly, calm, patient",
        "fun_fact": "Hospice monks in the Swiss Alps bred them to rescue lost travelers trapped in deep snow."
    },
    {
        "name": "Saluki",
        "animal": "Dog",
        "origin": "Middle East / Fertile Crescent",
        "lifespan": "12-14 years",
        "size": "Large",
        "temperament": "Aloof, graceful, gentle, lightning-fast",
        "fun_fact": "One of the oldest dog breeds known, mummified alongside ancient Egyptian Pharaohs."
    },
    {
        "name": "Samoyed",
        "animal": "Dog",
        "origin": "Siberia, Russia",
        "lifespan": "12-14 years",
        "size": "Large",
        "temperament": "Friendly, gentle, adaptable, cheerful",
        "fun_fact": "Famous for the 'Sammy smile', an upturned mouth that stops drool from freezing in sub-zero cold."
    },
    {
        "name": "Schipperke",
        "animal": "Dog",
        "origin": "Belgium",
        "lifespan": "13-15 years",
        "size": "Small",
        "temperament": "Curious, quick, confident, alert",
        "fun_fact": "Nicknamed 'the little black devil' for its energetic, curious nature aboard canal boats."
    },
    {
        "name": "Scotch Terrier",
        "animal": "Dog",
        "origin": "Scotland",
        "lifespan": "11-13 years",
        "size": "Small",
        "temperament": "Independent, confident, loyal, spirited",
        "fun_fact": "Known as the only dog breed to have lived in the White House with three US presidents."
    },
    {
        "name": "Scottish Deerhound",
        "animal": "Dog",
        "origin": "Scotland",
        "lifespan": "8-11 years",
        "size": "Giant",
        "temperament": "Gentle, dignified, polite, calm indoors",
        "fun_fact": "Originally reserved exclusively for Scottish nobility to course large red deer."
    },
    {
        "name": "Scottish Terrier",
        "animal": "Dog",
        "origin": "Scotland",
        "lifespan": "12-15 years",
        "size": "Small",
        "temperament": "Feisty, independent, playful, loyal",
        "fun_fact": "Also known as the 'Scottie', recognized by its beard, short legs, and determined stance."
    },
    {
        "name": "Sealyham Terrier",
        "animal": "Dog",
        "origin": "Wales, United Kingdom",
        "lifespan": "12-14 years",
        "size": "Small",
        "temperament": "Funny, outgoing, calm, determined",
        "fun_fact": "Loved by Hollywood legends including Alfred Hitchcock, Cary Grant, and Humphrey Bogart."
    },
    {
        "name": "Shetland Sheepdog",
        "animal": "Dog",
        "origin": "Scotland (Shetland Islands)",
        "lifespan": "12-14 years",
        "size": "Small",
        "temperament": "Playful, energetic, bright, affectionate",
        "fun_fact": "Nicknamed the 'Sheltie'; excels at agility championships around the world."
    },
    {
        "name": "Shiba Inu",
        "animal": "Dog",
        "origin": "Japan",
        "lifespan": "12-16 years",
        "size": "Small",
        "temperament": "Alert, active, attentive, spirited",
        "fun_fact": "An ancient Japanese national treasure, famous for the viral Internet 'Doge' meme."
    },
    {
        "name": "Shih-Tzu",
        "animal": "Dog",
        "origin": "Tibet / China",
        "lifespan": "10-16 years",
        "size": "Small",
        "temperament": "Affectionate, playful, outgoing, charming",
        "fun_fact": "Shih-Tzu means 'Little Lion' in Mandarin; bred as royal house companions for Ming Dynasty emperors."
    },
    {
        "name": "Siberian Husky",
        "animal": "Dog",
        "origin": "Siberia, Russia",
        "lifespan": "12-14 years",
        "size": "Medium",
        "temperament": "Loyal, mischievous, outgoing, gentle",
        "fun_fact": "Balto, the famous sled dog that delivered lifesaving diphtheria serum in 1925 Alaska, was a Husky."
    },
    {
        "name": "Silky Terrier",
        "animal": "Dog",
        "origin": "Australia",
        "lifespan": "12-15 years",
        "size": "Small",
        "temperament": "Friendly, quick, inquisitive, joyful",
        "fun_fact": "Features a fine, human-like glossy blue and tan coat that parts down the spine."
    },
    {
        "name": "Soft-Coated Wheaten Terrier",
        "animal": "Dog",
        "origin": "Ireland",
        "lifespan": "12-14 years",
        "size": "Medium",
        "temperament": "Happy, energetic, devoted, playful",
        "fun_fact": "Greets family with the famous 'Wheaten greetin', exuberantly jumping up to show affection."
    },
    {
        "name": "Staffordshire Bull Terrier",
        "animal": "Dog",
        "origin": "United Kingdom",
        "lifespan": "12-14 years",
        "size": "Medium",
        "temperament": "Courageous, intelligent, affectionate, playful",
        "fun_fact": "Nicknamed the 'Nanny Dog' in Britain for their legendary patience and affection toward children."
    },
    {
        "name": "Standard Poodle",
        "animal": "Dog",
        "origin": "Germany / France",
        "lifespan": "12-15 years",
        "size": "Large",
        "temperament": "Athletic, proud, remarkably intelligent, active",
        "fun_fact": "Originally bred as water retrievers; 'poodle' comes from the German word 'pudeln' (to splash)."
    },
    {
        "name": "Standard Schnauzer",
        "animal": "Dog",
        "origin": "Germany",
        "lifespan": "13-16 years",
        "size": "Medium",
        "temperament": "Fearless, smart, lively, loyal",
        "fun_fact": "The prototype schnauzer that appeared in paintings by Albrecht Dürer and Rembrandt."
    },
    {
        "name": "Sussex Spaniel",
        "animal": "Dog",
        "origin": "United Kingdom",
        "lifespan": "11-13 years",
        "size": "Medium",
        "temperament": "Calm, cheerful, affectionate, friendly",
        "fun_fact": "Famous for its unique golden-liver coat color found in no other spaniel."
    },
    {
        "name": "Tibetan Mastiff",
        "animal": "Dog",
        "origin": "Tibet",
        "lifespan": "10-12 years",
        "size": "Giant",
        "temperament": "Independent, reserved, deeply protective, calm",
        "fun_fact": "Nomads used them to guard camps; Marco Polo described them as 'tall as a donkey and loud as a lion'."
    },
    {
        "name": "Tibetan Terrier",
        "animal": "Dog",
        "origin": "Tibet",
        "lifespan": "12-15 years",
        "size": "Medium",
        "temperament": "Affectionate, loyal, sensitive, gentle",
        "fun_fact": "Known as the 'Holy Dog of Tibet', treasured as lucky charms by Buddhist monks."
    },
    {
        "name": "Toy Poodle",
        "animal": "Dog",
        "origin": "France",
        "lifespan": "14-18 years",
        "size": "Small",
        "temperament": "Alert, intelligent, lively, eager",
        "fun_fact": "Weighs only 4 to 6 pounds but retains the high intelligence and elegance of standard poodles."
    },
    {
        "name": "Toy Terrier",
        "animal": "Dog",
        "origin": "United Kingdom / United States",
        "lifespan": "12-16 years",
        "size": "Small",
        "temperament": "Spirited, alert, loyal, playful",
        "fun_fact": "Also called the English Toy Terrier, famous for sleek coats and candle-flame shaped ears."
    },
    {
        "name": "Vizsla",
        "animal": "Dog",
        "origin": "Hungary",
        "lifespan": "12-14 years",
        "size": "Medium",
        "temperament": "Affectionate, gentle, energetic, loyal",
        "fun_fact": "Called the 'Velcro dog' because they love to stay attached right next to their owner's side."
    },
    {
        "name": "Walker Hound",
        "animal": "Dog",
        "origin": "United States",
        "lifespan": "12-13 years",
        "size": "Large",
        "temperament": "Friendly, brave, energetic, relentless tracker",
        "fun_fact": "Developed in Kentucky from Virginia hounds by breeder Thomas Walker in the 1700s."
    },
    {
        "name": "Weimaraner",
        "animal": "Dog",
        "origin": "Germany",
        "lifespan": "11-13 years",
        "size": "Large",
        "temperament": "Energetic, friendly, fearless, alert",
        "fun_fact": "Nicknamed the 'Gray Ghost' due to their ghostly silver-gray coat and amber eyes."
    },
    {
        "name": "Welsh Springer Spaniel",
        "animal": "Dog",
        "origin": "Wales, United Kingdom",
        "lifespan": "12-15 years",
        "size": "Medium",
        "temperament": "Loyal, affectionate, playful, energetic",
        "fun_fact": "Always recognized by a rich red-and-white coat pattern and smaller vine-leaf ears."
    },
    {
        "name": "West Highland White Terrier",
        "animal": "Dog",
        "origin": "Scotland",
        "lifespan": "12-16 years",
        "size": "Small",
        "temperament": "Friendly, hardy, confident, entertaining",
        "fun_fact": "Affectionately called the 'Westie', bred with pure white fur so hunters could spot it easily in the heather."
    },
    {
        "name": "Wheaten Terrier",
        "animal": "Dog",
        "origin": "Ireland",
        "lifespan": "12-14 years",
        "size": "Medium",
        "temperament": "Lively, affectionate, intelligent, playful",
        "fun_fact": "Traditional all-purpose Irish farm dog known for its silky warm wheat-colored coat."
    },
    {
        "name": "Whippet",
        "animal": "Dog",
        "origin": "United Kingdom",
        "lifespan": "12-15 years",
        "size": "Medium",
        "temperament": "Gentle, calm indoors, lightning-fast runner",
        "fun_fact": "Capable of accelerating up to 35 mph (56 km/h), often called the poor man's racehorse."
    },
    {
        "name": "Wirehaired Pointer",
        "animal": "Dog",
        "origin": "Germany",
        "lifespan": "12-14 years",
        "size": "Large",
        "temperament": "Enthusiastic, eager, determined, loyal",
        "fun_fact": "Has a harsh wire coat that acts like armor against dense briars and cold weather."
    },
    {
        "name": "Yorkshire Terrier",
        "animal": "Dog",
        "origin": "United Kingdom",
        "lifespan": "11-15 years",
        "size": "Small",
        "temperament": "Brave, determined, lively, affectionate",
        "fun_fact": "Despite their diminutive size, Yorkies were originally bred to catch rats in textile mills."
    },
    {
        "name": "Bluetick Coonhound",
        "animal": "Dog",
        "origin": "United States",
        "lifespan": "11-12 years",
        "size": "Large",
        "temperament": "Friendly, energetic, intelligent, loyal",
        "fun_fact": "Its name comes from the dark blue ticking on its white coat; it was bred in the United States to trail raccoons by scent."
    },
    {
        "name": "Dandie Dinmont Terrier",
        "animal": "Dog",
        "origin": "Scotland",
        "lifespan": "12-15 years",
        "size": "Small",
        "temperament": "Independent, confident, intelligent, affectionate",
        "fun_fact": "Named after a farmer character in Sir Walter Scott's novel Guy Mannering."
    },
    {
        "name": "Wire Fox Terrier",
        "animal": "Dog",
        "origin": "England",
        "lifespan": "12-15 years",
        "size": "Small",
        "temperament": "Alert, energetic, confident, playful",
        "fun_fact": "Bred in England to flush foxes out of their dens, which is how it got its name."
    },
]
