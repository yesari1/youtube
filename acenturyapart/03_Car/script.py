# Buying a Car in 1926 vs 2026: full VO script. (chunk id, gap before chunk s, [(sentence id, text)])
# Facts + sources: ../../Research/03_Car_1926_vs_2026_Arastirma.md
CHUNKS = [
 ("hook", 0.3, [
  ("h1", "January, nineteen twenty-six. Walk into a Ford dealer anywhere in America, and a brand new Model T touring car costs two hundred and ninety dollars."),
  ("h2", "Today, the average new car in America sells for about fifty-one thousand."),
  ("h3", "So was buying a car a hundred years ago really that cheap?"),
  ("h4", "Let's buy one in each year, and find out. Same driveway. One hundred years apart."),
 ]),
 ("price", 1.0, [
  ("p1", "Start with the money."),
  ("p2", "Prices in America are about nineteen times higher today than in nineteen twenty-six. So that two hundred and ninety dollar Ford is about fifty-five hundred dollars in today's money."),
  ("p3", "But dollars hide something. A better way to compare is time."),
  ("p4", "In nineteen twenty-six, the average factory worker earned about fifty-seven cents an hour. The Model T cost him around five hundred hours of work. Roughly three months."),
  ("p5", "Today, the average manufacturing worker earns about thirty-seven dollars an hour. The average new car costs him nearly fourteen hundred hours. That's about eight months."),
  ("p6", "But that's not quite fair. The Model T was the cheapest car you could buy."),
  ("p7", "The cheapest new car in America today costs about twenty-two thousand dollars. Around six hundred hours of work. Only a little more than the Ford."),
 ]),
 ("credit", 1.2, [
  ("c1", "And most people didn't pay cash then either."),
  ("c2", "Henry Ford hated debt. So in nineteen twenty-three, Ford launched a plan where you put five dollars a week into a bank account, until you had saved enough for the car."),
  ("c3", "It didn't catch on. Other carmakers simply let you drive away now and pay later. By the mid nineteen twenties, about three out of four new cars in America were bought on credit."),
  ("c4", "Today, buying on time is the normal way. The average new car loan is about seven hundred and eighty-seven dollars a month, for almost six years. One in four new loans now runs seven years or longer."),
 ]),
 ("factory", 1.2, [
  ("f1", "So how could a car cost only three months of wages? The answer was in Detroit."),
  ("f2", "In nineteen thirteen, Ford started a moving assembly line. Instead of workers walking around a car, the car moved past the workers on a chain."),
  ("f3", "Building a Model T chassis dropped from about twelve and a half hours to about an hour and a half."),
  ("f4", "By the mid twenties, Ford's plants were turning out well over a million cars a year, and the price kept falling."),
  ("f5", "And in nineteen twenty-six, Ford did something else. It moved its factory workers to a five day, forty hour week. Henry Ford argued that people with more free time would buy more things. Including cars."),
  ("f6", "Today, much of that work is done by robots. A modern plant can finish a new car about every minute. But a modern car has thousands more parts, and far more electronics."),
 ]),
 ("car", 1.2, [
  ("k1", "So what did your two hundred and ninety dollars actually buy?"),
  ("k2", "A twenty horsepower engine, a top speed of around forty miles an hour, and a lot of things you had to do yourself."),
  ("k3", "On the cheapest Model T, an electric starter cost sixty-five dollars extra. Without it, you started the car with a hand crank at the front."),
  ("k4", "Get it wrong, and the crank could kick back hard enough to break your arm."),
  ("k5", "Inside, there was no gas pedal. You set the speed with a lever on the steering wheel, and worked three pedals with your feet. One of them was reverse."),
  ("k6", "And the color? For years, Ford famously sold the Model T in black only. Nineteen twenty-six is the year that finally changed. Closed models came in green and maroon."),
 ]),
 ("starter", 1.0, [
  ("s1", "The crank also decided who got to drive."),
  ("s2", "Cranking an engine took real strength. When the electric self starter arrived on Cadillacs in nineteen twelve, it opened the driver's seat to far more people."),
  ("s3", "Within a few years, carmakers were showing women in their ads as drivers, not just passengers."),
  ("s4", "Today, women hold just over half of all driver's licenses in America."),
 ]),
 ("today", 1.0, [
  ("t1", "Today, you press a button."),
  ("t2", "A typical new car makes well over a hundred and fifty horsepower, shifts by itself, and comes with airbags, a backup camera and automatic emergency braking."),
  ("t3", "Things that were expensive extras, or simply didn't exist, are now standard."),
 ]),
 ("license", 1.2, [
  ("l1", "Now drive it home."),
  ("l2", "In nineteen twenty-six, in much of America, you didn't need to pass any test to drive. Even by nineteen thirty, only fifteen states required a driving exam."),
  ("l3", "Many new owners learned on the road, in traffic, the day they bought the car."),
  ("l4", "Today, every state requires a license, a written test and a road test, and most new drivers spend months on a learner's permit first."),
 ]),
 ("roads", 1.2, [
  ("r1", "And the roads were dangerous."),
  ("r2", "There were no stop signs as we know them, few traffic lights, and many country roads were still dirt."),
  ("r2b", "Flat tires were a normal part of almost any long trip, so drivers carried a jack, a pump and a patch kit, and fixed them by the side of the road."),
  ("r3", "In nineteen twenty-six, America recorded about sixteen deaths for every hundred million miles driven."),
  ("r4", "Today, it's about one point two. Mile for mile, driving has become more than ten times safer."),
 ]),
 ("numbers", 1.2, [
  ("n1", "Here's the change that reshaped the country."),
  ("n2", "In nineteen twenty-six, there were about twenty-two million motor vehicles registered in America. Roughly one for every five people."),
  ("n3", "Today, there are around two hundred and eighty-five million. More than one for every licensed driver."),
  ("n4", "The car stopped being a purchase. It became the way America is built."),
 ]),
 ("verdict", 1.4, [
  ("e1", "So, nineteen twenty-six against twenty twenty-six."),
  ("e2", "Price. The average car takes almost three times as much work today. But the cheapest car costs about the same. Call it close."),
  ("e3", "Paying for it. Credit then, credit now. Only the loans got longer."),
  ("e4", "Safety. Hand cranks and dirt roads, against airbags and automatic brakes. An easy win for today."),
  ("e5", "A hundred years later, we still pay for cars the same way. We just get a lot more car for the money."),
  ("e6", "Would you take the two hundred and ninety dollar Ford, crank and all?"),
 ]),
]
if __name__ == "__main__":
    n = sum(len(t.split()) for _, _, ss in CHUNKS for _, t in ss)
    print(n, "words, ~", round(n / 2.45), "s")
