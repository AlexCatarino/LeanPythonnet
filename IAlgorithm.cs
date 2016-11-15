namespace LeanPythonnet
{
    public interface IAlgorithm
    {
        void Initialize();
        void OnData(int data);
    }
}