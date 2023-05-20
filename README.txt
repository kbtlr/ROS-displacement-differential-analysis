Included in this ZIP file is the package called ar_week5_test, to be used with ROS Melodic and python 2.7 on an Ubuntu 18.04 OS. What follows are steps on how to extract and compile the contents.
Assuming you already have a catkin workspace, extract the ar_week5_test folder in to the src directory. Enter, in this order:

cd ~/catkin_ws/
catkin_make -DPYTHON_EXECTUABLE=/usr/bin/python2.7
source devel/setup.bash
cd ~/catkin_ws/src/ar_week_5/
rosmake

The above sets up our workspace, ready for the code to be initialised and run.

cd ~/catkin_ws/src/ar_week_5/scripts
chmod +x compute_cubic_coeffs
chmod +x cubic_traj_planner
chmod +x plot_cubic_traj
chmod +x points_generator
cd ~/catkin_ws/src/ar_week_5/
roslaunch ar_week5_test cubic_traj_gen.launch

These lines initliases our python scripts and launches the ROS nodes, starting the program.

After 20 seconds, refresh the rqt_graph to see the connections. After a further 20 seconds, enter the topics in to the rqt_plot (Delete then press "/" in the search bar,
then select the acceleration, velocity and position trajectories to see the graph).



