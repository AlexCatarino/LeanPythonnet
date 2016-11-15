using System;
using Python.Runtime;
using ImpromptuInterface;

namespace LeanPythonnet
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                PythonEngine.Initialize();
                var scope = PythonEngine.ImportModule("BasicTemplateAlgorithm");
                var item = scope.GetAttr("BasicTemplateAlgorithm");
                
                dynamic dynamicAlgorithm = item;

                IAlgorithm algorithmInstance = Impromptu.ActLike<IAlgorithm>(dynamicAlgorithm);

                algorithmInstance.Initialize();

            }
            catch (Exception e)
            {
                Console.WriteLine(e.Message);
            }

            Console.Write("Done.");
            Console.ReadKey();
        }
    }
}